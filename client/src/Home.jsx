import React from 'react'
import Header from './components/Header'
import { Form, Button } from 'react-bootstrap'

export default function Homepage() {
    const formSubmit = () => {
        console.log('submit');
    }

    return (
        <>
            <Header></Header>
            <h1>Homepage</h1>
            <Form onSubmit={formSubmit}>
                <Form.Group>
                    <Form.Label>Transcript</Form.Label>
                    <Form.Control type="file" />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Video</Form.Label>
                    <Form.Control type="file" />
                </Form.Group>
                <Button type='submit'>Submit</Button>
            </Form>
        </>
    )
}
