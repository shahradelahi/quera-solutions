import React from "react";

import UserItem from "./UserItem";
import AverageAge from "./AverageAge";

import user from "./users.json";

const UserList = () => {
  const users = user;

  const handleAvg = () => {
    let avg = 0;

    let sum = 0;
    let counter = 0;

    users
      .filter(user => user.role === "admin")
      .map(user => {
        sum += user.age;
        counter++;
        return 1;
      });
    avg = sum / counter;
    //  console.log(avg)
    return avg;
  };

  return (
    <div>
      {users
        .filter(user => user.role === "user")
        .map(user => {
          return <UserItem name={user.name} />;
        })}

      <AverageAge average={handleAvg()} />
    </div>
  );
};

export default UserList;
