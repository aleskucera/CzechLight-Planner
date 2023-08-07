# CzechLight Management System

This is a short summary of the CESNET CzechLight project. This project is proof of concept of the management system for
the network consisting of the ROADM devices. The main goal of this project is to provide a simple and easy to use
management system.

The application is written in Django and communicates with devices through the Restconf API.

## Django Applications

The project consists of the following Django applications:

- **nodes** - application for listing/adding/editing/deleting nodes - ROADM devices (Line Degrees or Add/Drops) and
  Terminal Points which represent the end points of the network (e.g. datacenter, customer, etc.)
- **connection** - application for creating connections between nodes
- **network** - application mainly for management and communication with the network devices

## Future plans

- [ ] Add the new Django database model for the channels in channel plan (as discussed before there is need to have
  Channel Plan in the database but instead of having one ChannelPlan object it might be more suitable to have separate
  Channels). The advantages of this approach are:
    - Straightforward addition of new channels
    - Possibility to have different channel plans for different nodes
    - Straightforward creation of the JSON Channel Plan file
    - No need to have multiple database models for Channel Plan and Media Channel - the Channel Plan will be just a
      group of Channels and Media Channels will different group of Channels (Media Channels are just a subset of the
      Channel Plan for each device).
- [ ] Implement a Create Connection page where the user can select Termination Point A, Termination Point B, bandwidth
  and optionally the frequency. The application will then allow the user to select the path from the list of available
  paths. The application will then create a Connection object with the path and alternative_path fields filled in.
- [ ] Generate the configuration files for the devices based on the Connection objects.