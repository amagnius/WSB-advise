import React from 'react';

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
            <tr key={index}>
              <td>{stock.symbol}</td>
              <td>{stock.recommendation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StockList;