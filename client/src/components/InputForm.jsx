import React, { useState } from 'react'
import { Form, Button, Alert } from 'react-bootstrap'

export default function InputForm() {
    const [transcript, setTranscript] = useState(null);
    const [video, setVideo] = useState(null);
    const [error, setError] = useState(null);

    const fileFormats = {
        'transcript':['text/html', 'image/jpeg'],
        'video':['video/mp4']
    }

    const transcriptChange = (e) => {
        const selected = e.target.files[0];
        
        if (selected && fileFormats['transcript'].includes(selected.type)) {
            setTranscript(selected);
            setError('')
        } else {
            setTranscript(null);
            setError('Please use a transcript file (html)')
        }
    }

    const videoChange = (e) => {
        const selected = e.target.files[0];
        
        if (selected && fileFormats['video'].includes(selected.type)) {
            setVideo(selected);
            setError('')
        } else {
            setVideo(null);
            setError('Please use a video file (mp4)')
        }
    }

    const formSubmit = (e) => {
        e.preventDefault();
        console.log(video);
        console.log(transcript)
    }

    return (
        <>
            {error && <Alert variant='danger'>{error}</Alert>}
            <Form onSubmit={formSubmit}>
                <Form.Group controlId='transcript'>
                    <Form.Label>Transcript</Form.Label>
                    <Form.Control type="file" onChange={transcriptChange}/>
                </Form.Group>
                <Form.Group controlId='video'>
                    <Form.Label>Video</Form.Label>
                    <Form.Control type="file" onChange={videoChange}/>
                </Form.Group>
                <Button type='submit'>Submit</Button>
            </Form>
        </>
    )
}
