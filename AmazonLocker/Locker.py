from datetime import datetime, timedelta
from typing import Optional
import random
from Compartment import Compartment
from AccessToken import AccessToken
from Size import Size

class Locker:
    def __init__(self, compartments: list["Compartment"]):
        self.compartments = compartments
        self.access_token_mapping: dict[str, "AccessToken"] = {}
        
    def deposit_package(self, size: "Size") -> str:
        compartment = self._get_available_compartment(size)
        if compartment is None:
            raise Exception(f"No available compartment of size {size}")
        
        compartment.open()
        compartment.mark_occupied()
        access_token = self._generate_access_token(compartment)
        self.access_token_mapping[access_token.get_code()] = access_token
    
    def pickup(self, token_code: str) -> None:
        if not token_code:
            raise Exception("Invalid access token")
        access_token = self.access_token_mapping.get(token_code)
        if access_token is None:
            raise Exception("Invalid access token")
        if access_token.is_expired():
            raise Exception("Access token is expired")
        
        compartment = access_token.get_compartment()
        compartment.open()
        self._clear_deposit(access_token)
    
    def open_expired_compartments(self) -> None:
        for access_token in self.access_token_mapping.values():
            if access_token.is_expired():
                compartment = access_token.get_compartment()
                compartment.open()
    
    def _get_available_compartment(self, size: "Size") -> Optional["Compartment"]:
        for c in self.compartments:
            if c.get_size == size and not c.is_occupied():
                return c
        return None

    def _generate_access_token(self, compartment: "Compartment") -> "AccessToken":
        code = f"{random.randint(0, 999999):06d}"
        expiration = datetime.now() + timedelta(days=7)
        return AccessToken(code, expiration, compartment)
    
    def _clear_deposit(self, access_token: "AccessToken") -> None:
        compartment = access_token.get_compartment()
        compartment.mark_free()
        self.access_token_mapping.pop(access_token.get_code(), None)