const IsMarried =  ({value,onchangehandler}) => {
return( 
    <div>  
    <input name ="Is Married" type="checkbox" value={value}
    onChange={onchangehandler} /> {""}
    <label>Is Married</label> 
    </div>
 
)
}
export default IsMarried;