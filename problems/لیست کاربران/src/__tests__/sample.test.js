import '@testing-library/jest-dom/extend-expect'
import React from 'react'
import {render} from '@testing-library/react'

import UserList from '../UserList'

jest.mock('../users.json', () => {
  return [
    {
      name: 'user 1',
      age: 18,
      role: 'user',
    },
    {
      name: 'user 2',
      age: 18,
      role: 'user',
    },
    {
      name: 'admin 1',
      age: 30,
      role: 'admin',
    },
    {
      name: 'admin 2',
      age: 20,
      role: 'admin',
    },
  ]
})

test('users_list', () => {
  const {getByTestId, getAllByTestId} = render(<UserList />)

  const userNames = getAllByTestId('user-name')

  expect(userNames[0]).toHaveTextContent('user 1')
  expect(userNames[1]).toHaveTextContent('user 2')
  expect(getByTestId('average-age')).toHaveTextContent(25)
})
