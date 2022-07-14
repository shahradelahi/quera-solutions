import React from "react";

import UserItem from "./UserItem";
import AverageAge from "./AverageAge";

import user from "./users.json";

class UserList extends React.Component {
  constructor() {
    super();
    this.state = {
      people: user
    };
  }

  handleAvg = () => {
    let avg = 0;

    let sum = 0;
    let counter = 0;

    this.state.people
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

  render() {
    console.log(this.state.people);
    return (
      <div>
        {this.state.people
          .filter(user => user.role === "user")
          .map(user => {
            return <UserItem name={user.name} />;
          })}
     

        <AverageAge average={this.handleAvg()} />
      </div>
    );
  }
}

export default UserList;
