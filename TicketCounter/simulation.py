"""
Implementation of the main
simulation class
"""

import random
from arrays import Array
from llistqueue import Queue
from simpeople import TicketAgent, Passenger


class TicketCounterSimulation:
    """
    Create a simulation object
    """

    def __init__(self, num_agents, num_minutes, between_time, service_time):
        """
        Initialize simulator
        """
        # Parameters supplied by the user
        self._arrive_probability = 1.0 / between_time
        self._service_time = service_time
        self._num_minutes = num_minutes

        # Simulation components
        self._passengerQ = Queue()
        self._the_agents = Array(num_agents)
        for i in range(num_agents):
            self._the_agents[i] = TicketAgent(i + 1)

        # Computed during the simulation
        self._total_wait_time = 0
        self._num_passengers = 0

    def run(self):
        """
        Run the simulation
        using the parameters supplied earlier
        """
        for current_time in range(self._num_minutes + 1):
            self._handle_arrival(current_time)
            self._handle_begin_service(current_time)
            self._handle_end_service(current_time)

    def print_results(self):
        num_served = self._num_passengers - len(self._passengerQ)
        avg_time = float(self._total_wait_time) / num_served
        print("")
        print("Number of passengers served = ", num_served)
        print("Number of passengers remaining in line = %d" %
              len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avg_time)

    def _handle_arrival(self, current_time):
        """
        Handles simulation rule #1
        """
        checker = random.random()
        if self._arrive_probability >= checker >= 0:
            self._num_passengers += 1
            self._passengerQ.enqueue(Passenger(self._num_passengers, current_time))
            print(f"Passenger {self._num_passengers} arrived.")

    def _handle_begin_service(self, current_time):
        """
        Handles simulation rule #2
        """
        for agent in self._the_agents:
            if agent.is_free() and len(self._passengerQ) > 0:
                try:
                    passenger = self._passengerQ.dequeue()
                    self._total_wait_time += current_time - passenger.time_arrived()
                    agent.start_service(passenger, self._service_time + current_time)
                    print(f"Agent {agent.id_num()} started serving passenger {passenger.id_num()}.")
                except AttributeError:
                    continue

    def _handle_end_service(self, current_time):
        """
        Handles simulation rule #3
        """
        for agent in self._the_agents:
            if agent.is_finished(current_time):
                passenger = agent.stop_service()
                print(f"Agent {agent.id_num()} stopped serving passenger {passenger.id_num()}.")


if __name__ == "__main__":
    simulator = TicketCounterSimulation(4, 12, 4, 3)
    simulator.run()
