/** @format */

import { useState, useEffect } from "react";
export default function useFriendStatus(friendId) {
  const [isOnline, setIsOnline] = useState(false);

  ChatRoom.subscribeToFriendStatus();

  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(!isOnline);
    }
  });
  return isOnline;
}
