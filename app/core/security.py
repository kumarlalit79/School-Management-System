from datetime import datetime, timedelta
from jose import jwt
import bcrypt
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def verify_password(
    plain_password: str,
    hashed_password: str
):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )
    

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    
    to_encode.update({
        "exp": expire
    })
    
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        return payload
    
    except Exception:
        return None
    

def get_current_user(
    token : str = Depends(oauth2_schema)
):
    payload = verify_access_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    return payload


def require_role(allowed_roles: list):
    
    def role_checker(
        current_user = Depends(get_current_user)
    ):
        user_role = current_user.get("role")

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )
        
        return current_user

    return role_checker
