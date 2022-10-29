

import Button from "./Button";

import myImage from "../compo/test.jpg"
const Contact = () =>{
return(
    <div>
   
    <div className="container">
        <div className="row">
            <div className="col-md-12">
                <h1>Contacts App</h1>
             <Button text="Add Contact" classes ="btn btn-primary float-right "/>  
            </div>
            <div className="col-md-12">
              <h4>My Contacts</h4>
            </div>
            <br/>
            <div className="col-md-6">
                <div className="card">
                    <div className="card-body">
                        <img src={myImage} alt="" width={80} className="img img-thumbnail"/>
                        <p><strong>Name:</strong>Khalid</p>
                                <p><strong>Email:</strong>xyz@gmail.com</p>
                                <p><strong>Address:</strong> Abc</p>
                                <p><strong>Is Married:</strong> No</p>
                                <p><strong>Gender:</strong> Male</p>
                                <hr/>
                                <Button text="Edit" classes= "btn btn-link"/>
                                <Button text="Delete" classes= "btn btn-link"/>    
                                
            </div>
          </div>
        </div>
      
      
              
                  </div>
                       </div>
                   </div>
               
           
)

}
export default Contact;