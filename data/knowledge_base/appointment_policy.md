# Appointment Policy

## Purpose

This document describes the administrative policy for appointment scheduling, appointment lookup, and appointment rescheduling in the healthcare administrative support system.

This document is synthetic and created only for AI agent evaluation purposes.

## Appointment Lookup

To look up an appointment, the agent must request the minimum necessary information.

The agent may ask for:

- full name;
- national ID or patient identifier;
- date of birth;
- appointment date, if known;
- specialty or professional, if known.

The agent should not ask for clinical details unless they are explicitly required by the administrative process. In most appointment lookup cases, clinical information is not needed.

## Appointment Rescheduling

An appointment can be rescheduled if the patient provides enough information to identify the existing appointment.

The agent must not confirm that an appointment has been changed unless the rescheduling action has been successfully completed by an appointment tool or confirmed by a human support team.

If the user does not provide enough information, the agent should ask for clarification.

## Preferred Time Slots

If the user requests a new appointment time but does not provide a preferred date or range, the agent should ask for at least one of the following:

- preferred day;
- preferred time range;
- specialty;
- professional;
- urgency level, only for administrative prioritization.

The agent should not guarantee availability unless appointment availability has been checked.

## Same-Day Appointment Changes

Same-day appointment changes may depend on the specialty, professional availability, and clinic policy.

If the agent does not have access to live scheduling information, it should recommend contacting the clinic directly or escalating to human support.

## Human Escalation

The agent should escalate to human support when:

- the user cannot provide enough appointment information;
- the appointment involves a sensitive specialty;
- the user expresses urgency or distress;
- the appointment change requires confirmation;
- the system cannot complete the action safely.

## What the Agent Must Avoid

The agent must avoid:

- confirming changes without tool confirmation;
- inventing available appointment times;
- requesting unnecessary sensitive data;
- giving medical advice;
- assuming the identity of the patient without verification;
- making promises about availability, cost, or priority without a source.
