        "compatibilityImpact": {"type":"string","minLength":1},
        "validation": {
            "type":"array",
            "items":{
                "type":"object",
                "additionalProperties":False,
                "required":["name","result"],
                "properties":{
                    "name":{"type":"string","minLength":1},
                    "result":{"enum":result_enum},
                    "evidence":{"type":"string","minLength":1},
                    "environment":{"type":"string","minLength":1},
                    "limitations":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True}
                }
            }
        },
        "limitations": {"type":"array","items":{"type":"string","minLength":1}},
        "reviewer": {"type":"string","minLength":1},
        "reviewedAt": {"type":"string","format":"date-time"},
        "artifact": {"type":"string","minLength":1,"description":"Commit, tag, digest, or artifact identifier to which the result applies."}
    },
    ["status","summary","filesChanged","validation","limitations"]
)

schemas["exception-record"] = schema_base(
    "exception-record",
    "Standards Exception",
    "Records a time-bounded deviation from a specific rule, including ownership, rationale, risk, compensating controls, approval, status, and closure.",
    {
        "id":{"type":"string","minLength":1},
        "ruleId":{"type":"string","minLength":1},
        "owner":{"type":"string","minLength":1},
        "reason":{"type":"string","minLength":1},
        "risk":{"type":"string","minLength":1,"description":"Human-readable risk statement retained for backward compatibility."},
        "riskLevel":{"enum":risk_enum,"description":"Optional normalized risk classification."},
        "compensatingControls":{"type":"array","items":{"type":"string","minLength":1},"minItems":1,"uniqueItems":True},
        "expiresOn":{"type":"string","format":"date"},
        "status":{"enum":["requested","approved","rejected","expired","closed"]},
        "approver":{"type":"string","minLength":1},
        "approvedOn":{"type":"string","format":"date"},
        "reviewOn":{"type":"string","format":"date"},
        "remediationPlan":{"type":"string","minLength":1},
        "closureEvidence":{"type":"string","minLength":1}
    },
    ["id","ruleId","owner","reason","risk","compensatingControls","expiresOn","status"]
)

schemas["project-manifest"] = schema_base(
    "project-manifest",
    "Project Standards Manifest",
    "Declares the selected project profile, languages, disciplines, platforms, frameworks, risk, exceptions, and project-specific composition metadata.",
    {
        "name":{"type":"string","minLength":1},
        "profile":{"type":"string","minLength":1},
        "secondaryProfiles":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "languages":{"type":"array","items":{"type":"string","minLength":1},"minItems":1,"uniqueItems":True},
        "disciplines":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "platforms":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "frameworks":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "risk":{"enum":risk_enum},
        "exceptions":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "owners":{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":True},
        "evidenceLocation":{"type":"string","minLength":1}
    },
    ["name","profile","languages","disciplines"]
)

schemas["risk-classification"] = schema_base(
    "risk-classification",
    "Risk Classification",
    "Records a change risk level, rationale, evaluated factors, required reviewers, rollback requirement, ownership, and reassessment triggers.",
    {
        "level":{"enum":risk_enum},
        "rationale":{"type":"string","minLength":1},
        "factors":{
