import React, { useState } from 'react'
import { Form, Button, Alert, Container } from 'react-bootstrap'
import axios from 'axios'
import { bodyparser } from 'body-parser'

export default function InputForm() {
    const [transcript, setTranscript] = useState(null);
    const [video, setVideo] = useState(null);
    const [error, setError] = useState(null);
    const [fields, setFields] = useState(null);


    const fileFormats = {
        'transcript':['text/html', '.vtt','text/plain'],
        'video':['video/mp4']
    }

    const transcriptChange = (e) => {
        const selected = e.target.files[0];
        
        const fileExtension = selected.name.split(".").pop();

        if (selected && fileFormats['transcript'].includes(selected.type)
        || fileFormats['transcript'].includes(fileExtension)) {
            setTranscript(fileExtension);
            setError('')
            fieldsChange(e);
        } else {
            setTranscript(null);
            setError('Please use a transcript file (.html, .txt, .vtt)')
        }
    }

    const videoChange = (e) => {
        const selected = e.target.files[0];
        
        if (selected && fileFormats['video'].includes(selected.type)) {
            setVideo(selected);
            setError('')
            fieldsChange(e);
        } else {
            setVideo(null);
            setError('Please use a video file (mp4)')
        }
    }

    const fieldsChange = (e) => {
        setFields({
            ...fields,
            [e.target.id]: e.target.value
        })
        console.log(fields)
    }

    const formSubmit = (e) => {
        e.preventDefault();

        //store files to database
        // axios.post(/uploadvid/, {video}).then(function(response){
        //     console.log(response)
        // })
        // axios.post(/uploadtext/, {transcript}).then(function(response){
        //     console.log(response)
        // })
        axios.post(/splice/, { fields }).then(function(response){
            console.log(response)
        })
        console.log(video);
        console.log(transcript);
    }

    return (
        <>
            <Container>
                {error && <Alert variant='danger'>{error}</Alert>}
                <br/>
                <h3 style={{textAlign: 'center'}}>
                    Insert a Video and Transcript to be Parsed
                </h3>
                <form method="POST" action="" enctype="multipart/form-data">
                    <div>
                        <label for="transcript"><b>Transcript</b></label>
                        <br/>
                        <input type="file" name="transcript" />
                    </div>
                    <br/>
                    <div>
                        <label for="video"><b>Video</b></label>
                        <br/>
                        <input type="file" name="video" />
                    </div>
                    <br/>
                    <Button type="submit" value="Submit">Submit</Button>
                </form>
                <br/>

                <div>
                    <h3 style={{textAlign: 'center'}}>Choose the Start and Stop Word</h3>
                <Form onSubmit={formSubmit} >
                    {/* <Form.Group controlId='transcript' name='transcript'>
                        <Form.Label>Transcript</Form.Label>
                        <Form.Control type="file" onChange={transcriptChange}/>
                    </Form.Group>
                    <Form.Group controlId='video' name='video'>
                        <Form.Label>Video</Form.Label>
                        <Form.Control type="file" onChange={videoChange}/>
                    </Form.Group> */}
                    <Form.Group controlId='start'>
                        <Form.Label>Start Word</Form.Label>
                        <Form.Control type="text" onChange={fieldsChange}/>
                    </Form.Group>
                    <Form.Group controlId='stop'>
                        <Form.Label>Stop Word</Form.Label>
                        <Form.Control type="text" onChange={fieldsChange}/>
                    </Form.Group>
                    <Button type='submit'>Submit</Button>
                </Form>
                <a href="/returnfile" target="blank"><button class='btn btn-default'>Download!</button></a>
                </div>
            </Container>
        </>
    )
}
