/** @format */

export default function FreindRequest() {
  const all_freinds = userId => null;
  const requests = () => null;
  const rejects = () => null;

  const all_followers = () => null;
  const following = () => null;

  const acceptRequest = e => console.log(e);
  const declineRequest = e => console.log(e);
  return (
    <div className="w3-card-4 w3-dark-grey">
      <div className="w3-container w3-center">
        <h3>Friend request</h3>
        <img src="img_avatar3.png" alt="Avatar" style="width:80%" />
        <h5>John Doe</h5>
        <button onClick={acceptRequest} className="w3-button w3-green">
          Accept
        </button>
        <button onClick={declineRequest} className="w3-button w3-red">
          Decline
        </button>
      </div>
    </div>
  );
}
