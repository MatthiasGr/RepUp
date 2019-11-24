import React, {Component} from 'react';
import withStyles from '@material-ui/styles/withStyles';
import {withRouter} from 'react-router-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import InstructionDialog from './dialogs/InstructionDialog';
import SwipeDialog from './dialogs/SwipeDialog';
import Developers from "./developers";
import Topbar from './Topbar';
import Leaders from "./leaders";
//import StickyBox from "react-sticky-box/dist/esnext";
import Account from './img/account.png';

const styles = theme => ({
    root: {
        flexGrow: 1,
        overflow: 'hidden',
        backgroundSize: 'cover',
        backgroundPosition: '0 400px',
        paddingBottom: 150
    },
    grid: {
        width: 1200,
        marginTop: 40,
        [theme.breakpoints.down('sm')]: {
            width: 'calc(100% - 20px)'
        }
    },
    paper: {
        padding: theme.spacing(3),
        textAlign: 'left',
        color: theme.palette.text.secondary,
    },
    rangeLabel: {
        display: 'flex',
        justifyContent: 'space-between',
        paddingTop: theme.spacing(2)
    },
    topBar: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginTop: 32
    },
    outlinedButtom: {
        textTransform: 'uppercase',
        margin: theme.spacing(1)
    },
    actionButtom: {
        textTransform: 'uppercase',
        margin: theme.spacing(1),
        width: 152
    },
    blockCenter: {
        padding: theme.spacing(2),
        textAlign: 'center'
    },
    block: {
        padding: theme.spacing(2),
    },
    box: {
        marginBottom: 40
    },
    inlining: {
        display: 'inline-block',
        marginRight: 10
    },
    buttonBar: {
        display: 'flex'
    },
    alignRight: {
        display: 'flex',
        justifyContent: 'flex-end'
    },
    noBorder: {
        borderBottomStyle: 'hidden'
    },
    loadingState: {
        opacity: 0.05
    },
    loadingMessage: {
        position: 'absolute',
        top: '40%',
        left: '40%'
    },

    sidenav: {
        width: "160px",
        position: "fixed",
        zIndex: "1",
        overflowX: "hidden",
        top: "20px",
        right: "10px"
    },


});

const right_box = {
    width: "300px",
  paddingRight: "70px",
    float: "right",
    zIndex: "5",
};

class Main extends Component {

    state = {
        learnMoredialog: false,
        getStartedDialog: false,
        leaders: [],
        developers: []
    };

    componentDidMount() {
      // TODO: Correct URL for leaderboard
        // http://jsonplaceholder.typicode.com/users
        fetch('https://my-json-server.typicode.com/gereonelvers/RepUp_spoofAPI/users')
            .then(res => res.json())
            .then((data) => {
                data = data.sort((a, b) => a.score - b.score)
                this.setState({leaders: data})
            })
            .catch(console.log)

        // TODO: Correct URL for recents
        // http://jsonplaceholder.typicode.com/users
        fetch('https://my-json-server.typicode.com/gereonelvers/RepUp_spoofAPI/users1')
            .then(res => res.json())
            .then((data) => {
                data = data.sort((a, b) => a.score - b.score)
                this.setState({developers: data})
            })
            .catch(console.log)

        // TODO: insert "Me"-URL
        this.getData()
    }

  getData(url) {
    let xhr = new XMLHttpRequest();
    xhr.addEventListener('load', () => {
      // TODO: Fix API call
      // return JSON.parse(xhr.responseText)
    });
    xhr.open('GET', url)
    xhr.send()
    }

    openDialog = (event) => {
        this.setState({learnMoredialog: true});
    }

    dialogClose = (event) => {
        this.setState({learnMoredialog: false});
    }

    openGetStartedDialog = (event) => {
        this.setState({getStartedDialog: true});
    }

    closeGetStartedDialog = (event) => {
        this.setState({getStartedDialog: false});
    }

    render() {
        const {classes} = this.props;
        let persName = document.getElementById('persName');
        let persPoints = document.getElementById('persPoints');

        this.getData()


        return (
            <React.Fragment>
                <CssBaseline/>
                <Topbar/>
{/*
                <StickyBox offsetTop={200} offsetBottom={20}>
                    <Grid style={right_box}>
                        <Paper className={classes.paper}>
                          <Grid container spacing={"12"}>
                            <Grid item xs={"3"}>
                              <img src={Account}/>
                            </Grid>
                            <Grid item xs={"9"}>
                            <div className={classes.box} xs>
                                <Typography style={{textTransform: 'uppercase'}} color='secondary' gutterBottom>
                                    You
                                </Typography>
                                <Typography variant="body2" gutterBottom>
                                  <text id={"persName"}>First Lastname</text> <br/>
                                  <text id={"persPoints"}>420pts</text>
                                </Typography>
                            </div>
                            </Grid>
                          </Grid>
                        </Paper>
                    </Grid>
                </StickyBox>*/}

                <div className={classes.root}>
                    <Grid container justify="center">
                        <Grid spacing={4} alignItems="center" justify="center" container className={classes.grid}>
                            <Grid container item xs={12}>
                                <Grid item xs={12}>
                                    <Paper className={classes.paper}>
                                        <div>
                                            <div className={classes.box}>
                                                <Typography color='primary' gutterBottom>
                                                    <h2>Leaderboard</h2>
                                                    <Leaders leaders={this.state.leaders}/>
                                                </Typography>
                                            </div>
                                        </div>
                                    </Paper>
                                </Grid>
                            </Grid>
                            <Grid container item xs={12}>
                                <Grid item xs={12}>
                                    <div>
                                        <div className={classes.box}>
                                            <Typography color='secondary' gutterBottom>
                                                Recent Activity
                                            </Typography>
                                            <Typography variant="body1" gutterBottom>
                                                <Developers developers={this.state.developers}/>
                                            </Typography>
                                        </div>
                                    </div>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Grid>
                    <SwipeDialog
                        open={this.state.learnMoredialog}
                        onClose={this.dialogClose}/>
                    <InstructionDialog
                        open={this.state.getStartedDialog}
                        onClose={this.closeGetStartedDialog}
                    />
                </div>
            </React.Fragment>
        )
    }
}

export default withRouter(withStyles(styles)(Main));
