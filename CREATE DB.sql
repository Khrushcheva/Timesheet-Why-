CREATE DATABASE TimesheetWhy;
GO
CREATE SCHEMA Mainschema;
GO
CREATE TABLE Mainschema.Project (
	Project_ID INT PRIMARY KEY,
	Project_Name NVARCHAR(100) NOT NULL,
	Project_Description NVARCHAR(1000) NULL
);
GO
CREATE TABLE Mainschema.WorkType (
	WorkType_ID INT PRIMARY KEY,
	Project_ID INT NOT NULL REFERENCES Mainschema.Project(Project_ID),
	WorkType_Name NVARCHAR(100) NOT NULL,
	WorkType_Description NVARCHAR(1000) NULL
);
GO
CREATE TABLE Mainschema.TimesheetRecord (
	Project_ID INT REFERENCES Mainschema.Project(Project_ID),
	WorkType_ID INT REFERENCES Mainschema.WorkType(WorkType_ID),
	StartDateTime DATETIME NOT NULL,
	EndDateTime DATETIME NOT NULL,
	Value NVARCHAR(1000) NOT NULL,
	WorkDescription NVARCHAR(1000) NOT NULL,
	Documents NVARCHAR(2500) NOT NULL,
	Duration TIME NOT NULL,
	WorkPrice MONEY NULL,
	PRIMARY KEY (Project_ID, WorkType_ID, StartDateTime, EndDateTime)
);
GO
CREATE TABLE Mainschema.ProjectWorkTypePrice (
	Project_ID INT REFERENCES Mainschema.Project(Project_ID),
	WorkType_ID INT REFERENCES Mainschema.WorkType(WorkType_ID),
	StartDateTime DATETIME NOT NULL,
	EndDateTime DATETIME NOT NULL,
	HourPrice MONEY NULL,
	PRIMARY KEY (Project_ID, WorkType_ID, StartDateTime, EndDateTime)
)