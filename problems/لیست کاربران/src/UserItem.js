import React from 'react'

const UserItem = ({name}) => {
  return (
    <div className="card">
      <img
        src={`https://api.adorable.io/avatars/200/${name}.png`}
        alt="avatar"
      />
      <h3 data-testid="user-name">{name}</h3>
    </div>
  )
}

export default UserItem
