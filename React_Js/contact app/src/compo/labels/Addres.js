

const Addres = ({home,type,classes,value,onchangehandler}) => {
  return (
    <div className="form-group">
            <label>Address :</label>
            <textarea className="form-control" rows="5" onChange={onchangehandler} value={value}></textarea>
            </div>
  )
}

export default Addres;
