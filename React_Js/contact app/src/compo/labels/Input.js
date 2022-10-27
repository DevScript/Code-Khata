const Input = ({text, onchangehandler,label ,value}) =>{
    return(
       <div>
       <div className="form-group">
            <label >{label} </label>
            <input type={text} className="form-control" onChange={onchangehandler} value={value} />
            
        </div>
       
        </div>
    )
}
export default Input;