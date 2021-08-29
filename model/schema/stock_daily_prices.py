from datetime import datetime
from sqlalchemy import (DECIMAL, Column, DateTime, Interger, 
String, BIGINT)
from utils import Base


class StockDailyPrices(Base):
    __tablename__ = 'stock_daily_prices'
    
    id = Column(Interger, primary_key=True, autoincrement=True)
    symbol = Column(String(20), nullable=False)
    price_date = Column(DateTime, nullable=False)
    open_price = Column(DECIMAL(11,6)) 
    high_price = Column(DECIMAL(11,6))
    low_price = Column(DECIMAL(11,6))
    close_price = Column(DECIMAL(11,6))
    adj_close_price = Column(DECIMAL(11,6))
    volume = Column(BIGINT(20))
    created_at = Column(DateTime, default=datetime.utcnow) 
    updated_at = Column(DateTime, default=datetime.utcnow)
    updated_by = Column(String(30))