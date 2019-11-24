import React from 'react';
import Card from "@material-ui/core/Card";
import Account from "./img/account.png";

let divStyle = {
    padding: "5px",
    paddingBottom: "10px",
    textAlign: "center"
};

const Developers = ({ developers }) => {
    return (
        <div style={divStyle}>
            {developers.map((developers) => (

                <div style={divStyle}>
                    <Card elevation={1} style={divStyle}>
                        <div align={"left"} style={{
                            display: 'flex',
                            alignItems: 'center',
                        }}><img src={Account} alt={"Account"}/><text>{developers.name}</text></div>
                        <div align={"right"} style={{
                            display: 'right',
                            alignItems: 'right',
                        }}><text>{developers.username}</text></div>
                    </Card>
                </div>

            ))}
        </div>
    )
};

export default Developers