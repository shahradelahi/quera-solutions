import '@testing-library/jest-dom/extend-expect'
import React from 'react'
import Timer from '../Timer'
import {render, act, fireEvent} from '@testing-library/react'

beforeAll(() => {
  jest.useFakeTimers()
})
afterAll(() => {
  jest.useRealTimers()
})

test('test timer', () => {
  const {getByTestId} = render(<Timer />)

  for (let i = 1; i < 10; i++) {
    act(() => jest.advanceTimersByTime(1001))
    expect(getByTestId('time')).toHaveTextContent(i)
  }
})

test('test buttons', () => {
  const {getByTestId} = render(<Timer />)

  const time = getByTestId('time')
  const resume_button = getByTestId('resume-button')
  const stop_button = getByTestId('stop-button')
  const reset_button = getByTestId('reset-button')

  expect(time).toHaveTextContent(0)

  act(() => jest.advanceTimersByTime(1001))
  expect(time).toHaveTextContent(1)

  act(() => jest.advanceTimersByTime(900))
  expect(time).toHaveTextContent(1)

  fireEvent.click(reset_button)
  expect(time).toHaveTextContent(0)

  act(() => jest.advanceTimersByTime(500))
  expect(time).toHaveTextContent(0)

  act(() => jest.advanceTimersByTime(501))
  expect(time).toHaveTextContent(1)

  fireEvent.click(stop_button)
  expect(time).toHaveTextContent(1)

  act(() => jest.advanceTimersByTime(1500))
  expect(time).toHaveTextContent(1)

  fireEvent.click(resume_button)
  expect(time).toHaveTextContent(1)

  act(() => jest.advanceTimersByTime(1200))
  expect(time).toHaveTextContent(2)
})
