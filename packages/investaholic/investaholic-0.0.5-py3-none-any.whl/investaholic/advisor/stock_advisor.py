from typing import Optional
from datetime import datetime as dt
from .advisor import Advisor
from investaholic_common.classes.position import Position
from investaholic_common.classes.proposal import Proposal
from investaholic_common.representation.position_representation import PositionRepresentation
from investaholic_common.representation.proposal_representation import ProposalRepresentation
import requests


class StockAdvisor(Advisor):
    def __init__(self):
        Advisor.__init__(self)

    def advise(self) -> Proposal:
        response = requests.post(f'{self._url}/proposals/users/{self.customer.id}')
        return ProposalRepresentation.as_object(response.json())

    def modify_position_quantity(self, position: Position, quantity: float) -> Optional[Position]:
        return self._modify_position(position, quantity=quantity)

    def close_position_scheduled(self, position: Position, closing_date: dt):
        return self._modify_position(position, closing_date=closing_date)

    def close_position_now(self, position: Position):
        return self._modify_position(position)

    def _modify_position(self, position: Position, **kwargs):
        self._validate_position(position)

        if (quantity := kwargs.get('quantity')) is not None:
            query_string = {'quantity': quantity}
        elif (closing_date := kwargs.get('closing_date')) is not None:
            query_string = {'closing_date': closing_date.strftime("%d-%m-%Y")}
        elif len(kwargs) == 0:
            query_string = {'closing_date': dt.now().strftime("%d-%m-%Y")}
        else:
            return

        response = requests.put(f'{self._url}/positions/proposals/{position.proposal_code}'
                                f'/tickers/{position.ticker}', params=query_string)

        return PositionRepresentation.as_object(response.json())

    def _validate_position(self, position: Position):
        # Check whether the given position exists in the backend
        self._validate_n_proposal(position.proposal_code)

        # Check whether position belongs to user
        user_proposals = PositionRepresentation.as_object(
            requests.get(f'{self._url}/positions/users/{self.customer.id}').json())

        if position not in [prop.positions for prop in user_proposals if prop.code == position.proposal_code]:
            raise ValueError('Position ')

    def remove_position(self, position: Position):
        self._validate_position(position)

        response = requests.delete(f'{self._url}/positions/proposals/{position.proposal_code}/'
                                   f'tickers/{position.ticker}')
        
        return PositionRepresentation.as_object(response.json())

    def __str__(self) -> str:
        return f'Stock advisor of {self.customer.name} {self.customer.surname} (ID: {self.customer.id})'
