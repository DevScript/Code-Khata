import { useState } from "react";

        const Test = () => {
                
            
            const [text,settext] = useState("");
                
                
                const changehandler = (e) =>{
                    settext(e.target.value);
                }
            
                // const Increase = () => {
                //     setcount (count + 1)
                // }
                // const Decrease = () => {
                //     setcount (count - 1)
                // }
                // const Reset = () => {
                //     setcount (0)
                // }

            return(
                        <div>

                            <h1>WellCome : {text}</h1>
                        
                            <input type={"text"}  onChange={(e) => (changehandler(e))}/>
                            {/* <button onClick={Increase}>Increase</button>
                            <button onClick={Decrease}>Decrease</button>
                            <button onClick={Reset}>Reset</button>
                             */}
                         </div>


            )
        }
        export default Test;