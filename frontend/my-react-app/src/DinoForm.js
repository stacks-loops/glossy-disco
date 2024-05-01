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
        {({ values }) => (
            <Form>
                <Field type="text" name="title" placeholder="Workout Title" />

                <FieldArray name="steps">
                    {({ push, remove }) => (
                        <div>
                            {values.steps.map((step, index) => (
                                <div key={step.id}>
                                    <Field type="text" name={`steps[${index}].exerciseName`} placeholder="Exercise Name" />
                                    <Field as="select" name={`steps[${index}].interval`}>
                                        <option value="daily">Daily</option>
                                        <option value="every2days">Every 2 Days</option>
                                    </Field>




                                    <button type="button" onClick={() => remove(index)}>Remove Step</button>
                                    </div>
                            ))}
                            <button type="button" onClick={() => push({ id: uuidv4(), exerciseName: '', description: '', sets: '', reps: '', interval: '' })}>Add Step</button>
                        </div>
                    )}
                </FieldArray>

                <button type="submit">Submit</button>


            </Form>


            
        )}
        </Formik>
    )
}

export default DinoForm;