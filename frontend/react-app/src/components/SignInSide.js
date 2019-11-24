import React, {createRef, useRef} from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import {Link, withRouter} from 'react-router-dom';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Text from "recharts/lib/component/Text";

const useStyles = makeStyles(theme => ({
    root: {
        height: '100vh',
    },
    image: {
        backgroundRepeat: 'no-repeat',
        backgroundColor: '#707070',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
    },
    paper: {
        margin: theme.spacing(8, 4),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

export default function SignInSide() {
    const classes = useStyles();
    let api_key_output;

    function handleClick() {
        api_key_output = document.getElementById("api_key").value;
        console.log(api_key_output)
        // TODO: Not functional, skipable for demo?
        let xhr = new XMLHttpRequest();
        xhr.timeout = 4000;
        /*xhr.addEventListener('load', () => {
            // update the state of the component with the result here
            console.log(xhr.responseText);
            if (xhr.status<='200'&&xhr.status<=300){
                window.location.href = "http://localhost:3000/#/main";
            } else {
            }

        });
        const errorHandler = () => {
            document.getElementById("login_error").innerText = "Error: API-Key incorrect!";
        }*/

        xhr.onreadystatechange = function() {
            if(this.readyState === XMLHttpRequest.DONE && this.status != 200){
                window.location.href = "http://localhost:3000/#/main";
            } else {
                document.getElementById("login_error").innerText = "Error: API-Key incorrect or network issue!";
            }
        }

        //xhr.addEventListener("timeout", errorHandler)

        xhr.open('POST', 'localhost:1234/api/user/login');
        // send the request
        xhr.send(JSON.stringify({token: api_key_output}))

    }


    return (
        <Grid container component="main" className={classes.root}>
            <CssBaseline />
            <Grid item xs={false} sm={4} md={7} className={classes.image} />
            <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
                <div className={classes.paper}>
                    <Avatar className={classes.avatar}>
                        <LockOutlinedIcon />
                    </Avatar>
                    <Typography component="h1" variant="h5">
                        Sign in
                    </Typography>
                    <form className={classes.form} noValidate>
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="api_key"
                            label="API Key"
                            name="api_key"
                            autoComplete="api_key"
                            autoFocus
                        />
                        <FormControlLabel
                            control={<Checkbox value="remember" color="primary" />}
                            label="Remember me"
                        />
                        {/*<Link*/}
                        {/*    type="submit"*/}
                        {/*    fullWidth*/}
                        {/*    variant="contained"*/}
                        {/*    color="primary"*/}
                        {/*    className='button'*/}
                        {/*    to={'/main'}*/}
                        {/*>*/}
                            <Button
                                type="submit"
                                fullWidth
                                variant="contained"
                                color="primary"
                                className='button'
                                onClick={handleClick.bind(this)}
                            >
                                Sign In
                            </Button>
                        {/*</Link>*/}
                        <p id={"login_error"}/>
                    </form>
                </div>
            </Grid>
        </Grid>
    );
}