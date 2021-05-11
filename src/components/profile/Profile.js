/** @format */

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { users } from "./profile.test";

export default function Profile() {
  let { username } = useParams();
  const [user, setUser] = useState();
  const [isLoading, setIsLoading] = useState(true);
  const [api, setApi] = useState(users);
  useEffect(() => {
    const findUser = username =>
      setUser(api.filter(p_list => p_list.user.username === username)[0]);
    findUser(username);
    setIsLoading(false);
  }, [username]);
  return (
    <div>
      {isLoading ? (
        <div>Loading...</div>
      ) : (
        <div>
          <div className="w3-card-4 w3-dark-grey">
            <div className="w3-container w3-center">
              <h3>{`${user.user.first_name} ${user.user.last_name}'s Profile`}</h3>
              <img
                src={user.image}
                alt={`${user.user.username}'s profile`}
                style={{ width: "80%" }}
              />
            </div>
            <button className="w3-button w3-green">Accept</button>
              <button className="w3-button w3-red">Decline</button>
          </div>
        </div>
      )}
    </div>
  );
}
