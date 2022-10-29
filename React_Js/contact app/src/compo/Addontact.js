

import Forms from "../layouts/Forms";
import Button from "./Button";
import FormSubmitButton from "./labels/FormSubmitButton";
import Input from "./labels/Input";
import Email from "./labels/Email";
import Addres from "./labels/Addres";
import IsMarried from "./labels/IsMarried";
import Gender from "./labels/Gender";
import Pic from "./labels/Pic";
import { useState } from "react";
const AddContact = () => {

    const [name, setName] = useState ("");
    const [email, setEmail] = useState ("")
    const [address ,setAddress] = useState ("")
    const [ismarried , setIsMarried] = useState ("")
    const [gender ,setGender] = useState ("")

    return(

        
        <div>
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <h1>Contact App</h1>
                        <Button text="Add Contact" classes ="btn btn-primary float-right "/>  
                    </div>
                    <br/>
                    <div className="col-md-12">
                        <div className="col-md-8">
                        <Pic  label="Choose-Image" type="file" className="form-control"/>
                        <Input label="Name" type="text" value={name} 
                       onchangehandler = {(e) =>{
                     setName (e.target.value )  
                    }
                        } />
                        <Email label="Email" type="email" className="form-control" 
                        value={email} 
                        onchangehandler = {(e) =>{
                      setEmail (e.target.value )  
                     }
                         }
                        />
                        <Addres label="home" rows= '5' type="textarea" classes= "form-control" 
                        value={address} 
                        onchangehandler = {(e) =>{
                      setAddress (e.target.value )  
                     }
                         }
                        />
                          <IsMarried label="Is Married?" type="checkbox" value={ismarried}
                          onchangehandler = {(e)=>{
                            setIsMarried(!ismarried)
                          }} />
                           <Gender type="radio" options={['Male', 'Female' , 'Other']}  classes="form-control"
                           value={gender}
                           onchangehandler = {()=>{
                            
                           }}
                            />
                           <FormSubmitButton className="btn btn-success" btntxt="Save User"/>
                           <Forms/>
                           
                           
                          
                        </div>
                    </div>
                </div>
                </div>
            </div>

        
    )
};
export default AddContact