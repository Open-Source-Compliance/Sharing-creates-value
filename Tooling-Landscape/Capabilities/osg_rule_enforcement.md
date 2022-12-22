| (CI/CD) OSG Rule Enforcement         | |
| ---------------- | ------------------------------------------------ |
| Mission          | • Ensure only compliant artifacts will leave the automated tool chain   |
| Responsibilities | • Break build, deployment or packaging as long as compliance violations exist  |
| Tasks            | • Verify compliance state <br>• Interrupt automated build/deployment processing in case of violations<br>• Log event and causes<br>• Alert   |
| Input            | • Automation event  |
| Output           | • „Confirmation“ or „break“ event – or any sort of recording of required action<br>• Log entry  |
| Comments         | • The key of this is to ensure that no non-compliant artifact will leave the process. It must not be CI/CD driven, but it should ensure that a check happens |

OSG = Open Source Governance
