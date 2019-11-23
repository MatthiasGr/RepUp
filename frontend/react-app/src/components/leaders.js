import React from 'react';
import Card from "@material-ui/core/Card";
import Account from "./img/account.png";

let divStyle = {
    padding: "5px",
    textAlign: "center"
};

let rightBound = {
    align: "right",
};

let leftBound = {
    align: "left",
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
};


const Leaders = ({ leaders }) => {
    return (
        <div style={divStyle}>
            {leaders.map((developers) => (

                <div style={divStyle}>
                        <div align={"left"} style={{
                            display: 'flex',
                            alignItems: 'center',
                        }}><img src={Account} alt={"Account"}/><text>{developers.name}</text></div>
                        <div align={"right"} style={{
                            display: 'right',
                            alignItems: 'right',
                        }}><text>{developers.username}</text></div>
                </div>

            ))}
        </div>
    )
};

export default Leaders