import React from 'react';
import Container from 'react-bootstrap/Container';
import Table from 'react-bootstrap/Table';
import 'bootstrap/dist/css/bootstrap.min.css';
import _ from 'lodash'
import moment from "moment";

class CurrenciesTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            top_currencies: []
        };
    }

    componentDidMount() {
        fetch("/api/v1/market/")
            .then(res => res.json())
            .then(
                (result) => {
                    let mrkets = _.filter(result, (item) => item.close !== null && item.latest_trade !== null);
                    let mrkets_currency_map = _.groupBy(mrkets, (item) => item.currency)
                    let sorted_markets = _.reverse(_.sortBy(mrkets_currency_map, (items) => {
                        return items.length;
                    })).slice(0, 20);
                    let top_currencies = sorted_markets.map((items) => {
                        let sorted_markets = _.reverse(_.sortBy(items, (item) => {
                            return moment(item.latest_trade);
                        }));
                        return sorted_markets[0];
                    });
                    this.setState({
                        top_currencies: top_currencies
                    });
                }
            );
    }

    render() {
        const {top_currencies} = this.state;
        return (
            <Table>
                <thead>
                <tr>
                    <th>Currency</th>
                    <th>Market</th>
                    <th>Price</th>
                    <th>Last trade</th>
                </tr>
                </thead>
                <tbody>
                {top_currencies.map(item => (
                    <tr>
                        <td>{item.currency}</td>
                        <td>{item.symbol}</td>
                        <td>{item.close}</td>
                        <td>{item.latest_trade}</td>
                    </tr>
                ))}
                </tbody>
            </Table>
        )
    }
}

function App() {
    return (
        <Container>
            <h1>Top currencies:</h1>
            <CurrenciesTable/>
        </Container>
    );
}

export default App;
