# Documentation Validation Checklist

**Purpose:** Ongoing quality validation for LLM-friendly documentation. Run regularly to ensure documentation remains comprehensive and reconstruction-capable.

---

## Validation Metadata

**Validation Date:** [YYYY-MM-DD]
**Validated By:** [Name/Team]
**Project Version:** [version]
**Overall Status:** ⚠️ PENDING / ✅ PASS / ⚠️ NEEDS ATTENTION / ❌ FAIL

---

## Validation Scope

**This validation applies ONLY to files inside `docs/` folder.**

✅ **Allowed:**
- Read/verify documentation files in `docs/`
- Read code/files outside `docs/` to verify documentation accuracy
- Update checkboxes in this validation file

❌ **Not Allowed:**
- Edit any files outside `docs/` folder
- Modify code during validation
- Change project configuration during validation

**Purpose:** Validate documentation quality, not code quality.

---

## How to Use This Validation

**For Template Maintainers:**
Check that template provides guidance for each item.

**For Project Teams:**
Check that your documentation contains actual information for each item.

**Validation Process:**
1. Uncheck all boxes (reset to `[ ]`)
2. Go through each section systematically
3. Check `[x]` only if criterion is fully met
4. Read code/files outside `docs/` as needed to verify accuracy
5. Document issues in Action Items section
6. Update metadata (date, validator, status)
7. If score <90%, create remediation plan

---

## Validation Score

**Total Items:** 100+
**Passed:** [count checked boxes]
**Score:** [Passed/Total]%

**Threshold:** 90% required for PASS

---

## 1. File Length & Token Optimization

**Target:** Each core file should be <150 lines, ~1,000 words (~1,500 tokens max)

- [ ] `docs/README.md` - ~110 lines, ~500 words
- [ ] `docs/AGENTS.md` - ~190 lines, ~800 words
- [ ] `docs/CODING_GUIDELINES.md` - ~200 lines, ~1,000 words
- [ ] `docs/CONTENT_OWNERSHIP.md` - Reference file (can be longer)
- [ ] `docs/features/TEMPLATE.md` - Template (concise)
- [ ] Root `README.md` - Short, ~30-50 lines

## 2. File Naming Consistency

**Rule:** UPPERCASE = structure/meta, lowercase = content

- [ ] All meta files use UPPERCASE (`README.md`, `AGENTS.md`, `CODING_GUIDELINES.md`, `CONTENT_OWNERSHIP.md`, `TEMPLATE.md`)
- [ ] All content files use lowercase (`architecture.md`, `installation.md`, `usage.md`, `testing.md`)
- [ ] Project folder follows pattern (`README.md` = meta, `worklog.md`/`roadmap.md`/`changelog.md` = content)
- [ ] No mixed case files
- [ ] Naming is consistent across all references

## 3. Structure & Scannability

**Target:** Clear hierarchy, scannable headers, no deep nesting

- [ ] Max 3 levels of headings (H1 → H2 → H3)
- [ ] Each section has clear, descriptive headers
- [ ] Bullet points used for lists (not long paragraphs)
- [ ] Code blocks properly formatted
- [ ] Tables used for comparison/mapping
- [ ] No walls of text (paragraphs <5 lines)

## 4. Content Organization

**Target:** Logical flow, clear purpose, no overlap

- [ ] Each file has single, clear purpose
- [ ] Related content grouped together
- [ ] Logical section order (strategy → execution → measurement)
- [ ] No circular references
- [ ] Information flows naturally (general → specific)

## 5. Cross-References & Navigation

**Target:** Easy navigation, no dead links, clear paths

- [ ] All internal links work
- [ ] Cross-references use relative paths
- [ ] "See X for details" pattern used consistently
- [ ] Quick Reference section provides jump points
- [ ] No duplicate content (reference instead)
- [ ] Clear "breadcrumb" context (where you are)

## 6. Single Source of Truth

**Target:** Each fact lives in ONE place only

- [ ] No duplicated information across files
- [ ] Content Ownership clearly defined
- [ ] References used instead of copying
- [ ] Templates separated from content
- [ ] Meta descriptions separated from actual content

## 7. LLM-Specific Optimizations

**Target:** Designed for AI comprehension and action

- [ ] File naming convention explicitly stated
- [ ] AGENTS.md clearly marked "For AI Assistants"
- [ ] Workflow steps numbered and clear
- [ ] Critical constraints marked with ❌/✅
- [ ] Examples provided for complex concepts
- [ ] Action items clearly marked
- [ ] Meta vs content distinction clear

## 8. Completeness & Consistency

**Target:** All required files present, consistent style

- [ ] All template files present in `docs/`
- [ ] All folders have purpose (no empty folders without .gitkeep)
- [ ] Consistent markdown style (headers, lists, code blocks)
- [ ] Consistent terminology throughout
- [ ] File structure diagram matches actual structure
- [ ] Last Updated dates present

## 9. Purpose Clarity

**Target:** Clear "what is this FOR" in each file

- [ ] Root README explains project purpose
- [ ] docs/README explains documentation structure
- [ ] AGENTS.md addresses LLMs directly
- [ ] CODING_GUIDELINES.md explains when/how to document
- [ ] CONTENT_OWNERSHIP.md clarifies what goes where
- [ ] project/README.md explains folder purpose (meta)
- [ ] features/TEMPLATE.md guides feature documentation

## 10. GitHub Integration

**Target:** Clear relationship with GitHub features

- [ ] docs/project purpose explained (fills gap between commits/PRs)
- [ ] worklog.md vs GitHub Issues distinction clear
- [ ] changelog.md vs GitHub Releases relationship defined
- [ ] roadmap.md vs GitHub Projects relationship defined

## 11. Expandability

**Target:** Clear growth path for complex projects

- [ ] Single file → folder pattern documented
- [ ] testing.md expandability noted
- [ ] features/ can grow (single file OR folder)
- [ ] Template supports both simple and complex projects

## 12. Git Status

**Target:** Clean staging, proper renames tracked

- [ ] All files properly staged
- [ ] Renames tracked by git (not delete + add)
- [ ] No unexpected changes
- [ ] .gitkeep files in place for empty folders

## 13. PROJECT RECONSTRUCTION TEST ⚠️

**Target:** Documentation alone is sufficient to rebuild the entire project from scratch

### 13.1. Technology Stack Reconstruction

- [ ] All dependencies listed with versions (language, frameworks, libraries)
- [ ] Technology choices explained with rationale (why X over Y)
- [ ] External services documented (APIs, databases, cloud services)
- [ ] Development tools specified (build tools, CLI tools, IDE requirements)
- [ ] Runtime requirements clear (Node version, Python version, etc.)

### 13.2. Architecture Reconstruction

- [ ] System components identified (all major modules/services)
- [ ] Component relationships mapped (how they connect/communicate)
- [ ] Data flow documented (how data moves through the system)
- [ ] Module organization explained (folder structure, file organization)
- [ ] Architectural patterns specified (MVC, microservices, event-driven, etc.)

### 13.3. Data & State Reconstruction

- [ ] Data structures documented (models, schemas, types)
- [ ] Database schemas defined (tables, relationships, indexes)
- [ ] File formats specified (config files, data files, naming conventions)
- [ ] State management explained (how state is stored and managed)
- [ ] Data transformations documented (pipelines, ETL processes)

### 13.4. Business Logic Reconstruction

- [ ] Business rules documented (what to process, what to skip, validation rules)
- [ ] Algorithms described (high-level pseudocode for complex operations)
- [ ] Workflows mapped (step-by-step processes from input to output)
- [ ] Edge cases documented (special handling, error scenarios)
- [ ] Processing rules clear (filtering, sorting, transformation logic)

### 13.5. Integration & APIs Reconstruction

- [ ] API contracts defined (endpoints, methods, parameters, responses)
- [ ] Integration points documented (external APIs, webhooks, services)
- [ ] Authentication/authorization explained (how security works)
- [ ] Event flows documented (pub/sub, events, messages)
- [ ] Interface specifications (UI components, CLI commands, programmatic APIs)

### 13.6. Configuration Reconstruction

- [ ] Environment variables listed (all required and optional vars)
- [ ] Config file structure documented (format, keys, default values)
- [ ] Configuration logic explained (how config affects behavior)
- [ ] Secrets management documented (where secrets go, how they're used)
- [ ] Multi-environment setup (dev, staging, prod differences)

### 13.7. Build & Deploy Reconstruction

- [ ] Build process documented (how to compile/bundle/package)
- [ ] Deployment process documented (how to deploy, where to deploy)
- [ ] Release process explained (versioning, tagging, changelog)
- [ ] CI/CD pipeline documented (if applicable)
- [ ] Infrastructure requirements (servers, resources, scaling)

### 13.8. Feature Implementation Reconstruction

- [ ] Each feature has implementation guide (how it works across modules)
- [ ] Feature-specific data documented (what data each feature uses)
- [ ] Feature workflows explained (end-to-end user/system flows)
- [ ] Feature configuration documented (how to enable/configure features)
- [ ] Feature dependencies mapped (what else is needed for this feature)

### 13.9. Core Concepts Reconstruction

- [ ] Domain knowledge documented (business domain, terminology)
- [ ] Key abstractions explained (patterns, principles used)
- [ ] Design principles stated (guiding principles for decisions)
- [ ] Naming conventions defined (files, variables, functions)
- [ ] Code organization rules (where different types of code go)

### 13.10. Decision History Reconstruction

- [ ] Architectural decisions recorded (ADRs - what, why, when)
- [ ] Trade-offs documented (what was gained/lost with each decision)
- [ ] Rejected alternatives noted (what was considered but not chosen)
- [ ] Migration paths documented (how to change from old to new)
- [ ] Technical debt tracked (known issues, why they exist, plans to fix)

### 13.11. Installation & Setup Reconstruction

- [ ] Prerequisites clear (what to install first)
- [ ] Step-by-step installation (platform-specific where needed)
- [ ] Verification steps (how to know setup worked)
- [ ] Troubleshooting guide (common issues and solutions)
- [ ] First-run instructions (what to do after installation)

### 13.12. Testing Reconstruction

- [ ] Testing strategy documented (what gets tested, approach)
- [ ] Test structure explained (how tests are organized)
- [ ] How to run tests (commands, flags, options)
- [ ] How to write tests (patterns, conventions, examples)
- [ ] Coverage expectations (what coverage is expected where)

---

## RECONSTRUCTION VALIDATION TEST

**Pass criteria:** A seasoned developer with NO access to code should be able to:

- [ ] Install all required dependencies from `installation.md`
- [ ] Understand system architecture from `architecture.md`
- [ ] Recreate all data models from architecture + features docs
- [ ] Implement all business logic from architecture + features docs
- [ ] Recreate all API contracts from architecture + features docs
- [ ] Configure the system from `usage.md` + `installation.md`
- [ ] Understand all design decisions from `architecture.md` + decision logs
- [ ] Build and deploy the system from documented processes
- [ ] Write appropriate tests from `testing.md` + feature docs
- [ ] Recreate ~80%+ of original functionality
 
**If ANY fail, documentation is insufficient for reconstruction.**

---

## Validation Process

- [ ] Read each core file as an LLM would (top to bottom)
- [ ] Verify token counts with `wc -l` and `wc -w`
- [ ] Check all cross-references click through
- [ ] Confirm no duplicate content
- [ ] Verify file naming consistency
- [ ] Test navigation flow
- [ ] Perform reconstruction thought experiment: Could you rebuild this?

## Success Criteria

- [ ] LLM can understand structure in <2 minutes
- [ ] All core files under 1,500 tokens
- [ ] Zero duplicate information
- [ ] Clear action paths for common tasks
- [ ] Expandable without breaking structure
- [ ] Passes reconstruction validation test

---

## Action Items (if validation fails)

**Critical Issues:**
- [ ][Issue description] - Owner: [name] - Due: [date]

**High Priority:**
- [ ][Issue description] - Owner: [name] - Due: [date]

**Medium Priority:**
- [ ][Issue description] - Owner: [name] - Due: [date]

**Low Priority:**
- [ ][Issue description] - Owner: [name] - Due: [date]

---

**Last Updated:** 2025-11-08
**Next Validation Due:** [Recommend: before major releases, or quarterly]
