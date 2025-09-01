
export default function AlertList({ alerts, onInvestigate }) {
  return (
    <ul style={{ listStyle: 'none', padding: 0 }}>
      {alerts.map(alert => (
        <li
          key={alert.id}
          style={{
            marginBottom: '15px',
            padding: '10px',
            borderRadius: '5px',
            border: '1px solid #ccc',
            backgroundColor: alert.risk_score === 'High' ? '#f8d7da' : '#fff3cd',
            boxShadow: '0 2px 5px rgba(0,0,0,0.1)'
          }}
        >
          <strong>Risk:</strong> {alert.risk_score} <br />
          <strong>Alert:</strong> {alert.text} <br />
          <button
            onClick={() => onInvestigate(alert.id)}
            style={{
              marginTop: '8px',
              backgroundColor: '#007bff',
              color: 'white',
              border: 'none',
              padding: '6px 12px',
              borderRadius: '3px',
              cursor: 'pointer',
              transition: 'background-color 0.3s ease',
            }}
            onMouseEnter={e => e.target.style.backgroundColor = '#0056b3'}
            onMouseLeave={e => e.target.style.backgroundColor = '#007bff'}
          >
            Mark as Investigated
          </button>
        </li>
      ))}
    </ul>
  );
}
