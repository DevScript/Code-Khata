


const Gender = ({options , classes, value}) => {
  return (
    <div>
        <label>Gender :</label>
        <br/>
{options.map ((option) => 

    <div>
        <input type="radio" value="Male" name="gender"  classes={classes}
        /> {option}
    </div>
)}

  </div>
  )
}

export default Gender;
