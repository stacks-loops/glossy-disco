import React from 'react'
import { Formik, Form, Field } from 'formik'
import { v4 as uuidv4 } from 'uuid'

const initialFormData = {
    title: '', 
    steps: []
}

const workoutStep = {
    exerciseName: '',
    description: '',
    sets: '',
    reps: '',
    interval: ''
}

function DinoForm() {
    return (
        <Formik 
        initialValues={initialFormData}
        onSubmit={(values) => console.log(values)}
        ></Formik>
    )
}

export default DinoForm;