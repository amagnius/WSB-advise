import React from 'react';
import Stock from './Stock';

const StockList = ({ title, stocks }) => {
  return (
    <div className="stock-list">
      <h2 style={{ fontSize: '2rem' }}>{title}</h2> {}
      {stocks.map((stock, index) => (
        <Stock key={index} ticker={stock.ticker} action={stock.action} />
      ))}
    </div>
  );
};

export default StockList;
