import Link from 'next/link';

export default function Customer() {
  // In a full application, fetch the customer’s purchase history and calendar data.
  return (
    <div>
      <h1>Customer's My-Page</h1>
      <div>
        <h2>Purchase History</h2>
        <ul>
          <li>
            <p>Asset Title Example</p>
            <Link href="/history-detail">
              <a>Detail</a>
            </Link>
          </li>
          {/* More purchase items here */}
        </ul>
      </div>
      <div>
        <h2>Calendar</h2>
        <p>[Calendar showing your request start/end dates]</p>
      </div>
    </div>
  );
}
