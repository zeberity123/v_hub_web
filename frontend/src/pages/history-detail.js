export default function HistoryDetail() {
    return (
      <div>
        <h1>Purchase History Detail</h1>
        <div>
          <p>Progress: 50%</p>
          <div style={{ background: '#ddd', width: '100%', height: '20px' }}>
            <div style={{ background: '#4caf50', width: '50%', height: '100%' }} />
          </div>
        </div>
        <div>
          <h2>Chat with Creator</h2>
          <textarea placeholder="Type your message here..." rows="4" cols="50" />
          <button>Send</button>
        </div>
      </div>
    );
  }
  