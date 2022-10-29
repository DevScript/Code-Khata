const Email = ({onchangehandler,email,label,value}) =>{
return (
    
    
    <div>
       <div className="form-group">
            <label >{label} </label>
            <input type={email} className="form-control"
            onChange={onchangehandler} value={value}/>
        </div>
        </div>
    

)
}
export default Email;