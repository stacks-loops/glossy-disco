import React from 'react'
import { Formik, Form, Field } from 'formik'
import { v4 as uuidv4 } from 'uuid'

const initialFormData = {
    title: '', 
    steps: [
        { id: uuidv4(), exerciseName: '', description: '', sets: '', reps: '', interval: '' }
    ]
}

// const workoutStep = {
//     exerciseName: '',
//     description: '',
//     sets: '',
//     reps: '',
//     interval: ''
// }

function DinoForm() {
    return (
        <Formik 
        initialValues={initialFormData}
        onSubmit={(values) => console.log(values)}
        >
        {({ values, setFieldValue }) => (
            <Form>
                <Field type="text" name="title" placeholder="Workout Title" />

                <button type="submit">Submit</button>
            </Form>
            
        )}
        </Formik>
    )
}

export default DinoForm;