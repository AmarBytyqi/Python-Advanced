from typing import List
from streamlit import status
import sqlite3
from models.category import Category, CategoryBase
from database import get_db_connection
from fastapi import APIRouter, HTTPException

@APIRouter("/")