import React from 'react'

const AverageAge = ({average}) => {
  return (
    <>
      <div className="break"></div>
      <div className="card">
        میانگین سن ادمین ها:‌ <span data-testid="average-age">{average}</span>
      </div>
    </>
  )
}

export default AverageAge
