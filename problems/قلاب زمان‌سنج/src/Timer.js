import React from 'react'
import {useTimer} from './use-timer'

function Timer() {
  const {seconds, resume, stop, reset} = useTimer()

  return (
    <div className="timer">
      <div className="time" data-testid="time">
        {seconds}
      </div>
      <div className="buttons">
        <button onClick={reset} data-testid="reset-button">
          شروع مجدد
        </button>
        <button onClick={resume} data-testid="resume-button">
          ادامه
        </button>
        <button onClick={stop} data-testid="stop-button">
          توقف
        </button>
      </div>
    </div>
  )
}

export default Timer
