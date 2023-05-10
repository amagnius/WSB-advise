import React from 'react';
import Stock from './Stock';

const StockList = ({ title, stocks }) => {
  return (
    <div className="stock-list">
      <h2>{title} Recommendations</h2>
      <table>
        <thead>
          <tr>
            <th>Stock Symbol</th>
            <th>Recommendation</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock, index) => (
            <Stock key={index} ticker={stock.ticker} action={stock.action} />
          ))}
        </tbody>
      </table>
    </div>
  );
};
          

export default StockList;

