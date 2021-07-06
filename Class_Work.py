class WorkClass:

    def __init__(self, ProjectID, WorkTypeID, StartDateTime, EndDateTime, Value, WorkDescription, Documents, HourPrice):
        self.ProjectID = ProjectID,
        self.WorkTypeID = WorkTypeID,
        self.StartDateTime = StartDateTime,
        self.EndDateTime = EndDateTime,
        self.Value = Value,
        self.WorkDescription = WorkDescription,
        self.Documents = Documents,
        self.HourPrice = HourPrice

    def CalculateDuration (self, StartDateTime, EndDateTime):
        self.Duration = StartDateTime - EndDateTime

    def CalculateWorkPrice (self, Duration, HourPrice):
        self.WorkPrice = Duration * HourPrice