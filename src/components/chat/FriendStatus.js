/** @format */

export default function FriendStatus({ friend: { id } }) {
  const isOnline = useFriendStatus(id);
  if (isOnline === null) {
  }
}
