import { useState,useEffect } from "react"

export function useTimer() {

  const [seconds, setSeconds] = useState(0)
  const [isStop, setIsStop] = useState(false)

  let timeOut
  useEffect(() => {
    // alert('hi')
    if (!isStop) {
      timeOut = setTimeout(() => {
        setSeconds(seconds + 1)
      }, 1000);
    }
  }, [seconds, isStop])
  const reset = () => {
    clearTimeout(timeOut)
    setSeconds(0)
  }

  const stop = () => {
    clearTimeout(timeOut)

    setIsStop(true)
  }

  const resume = () => {
    clearTimeout(timeOut)
    setIsStop(false)
  }

  return { seconds, resume, stop, reset }
}
