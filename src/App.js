import { useEffect, useState } from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import AlertList from './AlertList';

function App() {
  const [alerts, setAlerts] = useState([]);
  const [graphData, setGraphData] = useState(null);

  useEffect(() => {
    fetch('/alerts')
      .then(response => response.json())
      .then(data => setAlerts(data))
      .catch(error => console.error('Error fetching alerts:', error));

    fetch('/graph')
      .then(response => response.json())
      .then(data => setGraphData(data))
      .catch(error => console.error('Error fetching graph data:', error));
  }, []);

  const handleNodeClick = node => {
    alert(`Clicked node: ${node.id} (${node.group})`);
  };

  const markInvestigated = (id) => {
    fetch(`/alert/${id}/investigate`, { method: 'POST' })
      .then(response => {
        if (response.ok) {
          setAlerts(prev => prev.filter(alert => alert.id !== id));
        } else {
          alert('Failed to mark alert as investigated');
        }
      })
      .catch(() => alert('Network error'));
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Darknet Drug Trade Alerts</h1>
      {alerts.length === 0 ? (
        <p>No alerts found.</p>
      ) : (
        <AlertList alerts={alerts} onInvestigate={markInvestigated} />
      )}

      <h2>Network Graph</h2>
      {graphData ? (
        <ForceGraph2D
          graphData={graphData}
          nodeAutoColorBy="group"
          nodeLabel="id"
          onNodeClick={handleNodeClick}
          height={400}
          linkDirectionalArrowLength={6}
          linkDirectionalArrowRelPos={1}
          linkCurvature={0.1}
          d3AlphaDecay={0.05}
        />
      ) : (
        <p>Loading graph...</p>
      )}
    </div>
  );
}

export default App;
