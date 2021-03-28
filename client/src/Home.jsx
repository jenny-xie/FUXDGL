import React, { useState, useEffect } from 'react'
import Header from './components/Header'
import InputForm from './components/InputForm'

export default function Homepage() {
    const [time, setTime] = useState(0);
    useEffect(() => {
        fetch('/time').then(res => res.json()).then(data => {
            setTime(data.time);
        })
    },[])
    
    return (
        <>
            <Header></Header>
            <h1>Time: {time}</h1>
            <InputForm></InputForm>
        </>
    )
}
