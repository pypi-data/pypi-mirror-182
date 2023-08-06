=========
Changelog
=========

Development version
===================

Version 1.4.0, 2023-XX-XX
-------------------------

- Add `ConditionalCommand`
- Add `FunctionalCommand`
- Add `InstantCommand`
- Add `RunCommand`
- Add `PerpetualCommand`
- Add `ScheduleCommand`
- Add `StartEndCommand`
- Add `WaitCommand`
- Add `WaitUntilCommand`
- Add `ParallelRaceGroup`
- Add `ParallelDeadlineGroup`
- Add `Command.with_timeout`
- Add `Command.until`
- Add `Command.and_then`
- Add `Command.before_starting`
- Add `Command.along_with`
- Add `Command.race_with`
- Add `Command.deadline_with`
- Add `Command.perpetually`
- Add command suppliers support


Current versions
================

Version 1.3.0, 2022-XX-XX
-------------------------

- Various bugfixes and improvements
- Improve documentation
- Remove `ABCMeta` metaclass implementations for PyQt compatibility

Version 1.2.0, 2022-09-13
-------------------------

- Implement missing "cancel when activated" action condition
- Add `Command` unicode representation
- Add `SequentialCommandGroup` and `ParallelCommandGroup`
- Add official support for Python 3.7 and Python 3.8
- Require coverage be 100% for tests to pass

Version 1.1.2, 2022-09-01
-------------------------

- Fix metaclass conflict in `CommandBasedRobot`

Version 1.1.1, 2022-08-30
-------------------------

- Add prestart and postend execution
- Turn `CommandBasedRobot` into a proper template

Version 1.1.0, 2022-08-30
-------------------------

- Implement `Scheduler.execute`

Version 1.0.0, 2022-08-29
-------------------------

- Initial release
