# RevMeta Coding Codebook — 102 terms (source revision 2)

Registry: `revmeta-102-terms-source-v2`  
Checksums: `dist/manifest.json`

> Development-only RevMeta coding guidance. Previous source states are preserved in private provenance.

## revmeta:hasReviewDesign — review design

**Tier:** `CORE_FACET`  
**Definition:** Relates a review publication to the methodological review design realized by the reported review investigation, not merely to a synthesis technique, speed modifier, update mode, or publication genre label.

**Boundary:** Design values are not globally mutually exclusive. SystematicReviewDesign requires conjunction of review-level systematic framing + process realization; label alone and search alone are each insufficient.

### `revmeta:hasReviewDesign.NarrativeReviewDesign` — Narrative review design

**Depth:** `CORE_FACET`  
**Definition:** A review design explicitly presented as a narrative review or clearly organized as an author-led narrative review design rather than merely using narrative prose for synthesis.

**CODE WHEN**
- The publication explicitly identifies its review design as narrative review, or equivalent wording clearly names the design.

**DO NOT CODE WHEN**
- Do not infer this design merely because no systematic protocol is reported.
- Do not code it only because the results are written narratively.

**Boundary notes**
- Do not confuse with NarrativeSynthesis; design and synthesis method are independently coded.
- Lack of a systematic protocol is not positive evidence for narrative review design.

**Positive examples**
- The authors explicitly state that the review was conducted as a narrative review design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports a narrative review design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.IntegrativeReviewDesign` — Integrative review design

**Depth:** `CORE_FACET`  
**Definition:** A review design explicitly using an integrative review approach to combine heterogeneous forms of literature or evidence within one review design.

**CODE WHEN**
- The publication explicitly declares an integrative review or describes an integrative-review methodology as its design.

**DO NOT CODE WHEN**
- Do not infer from the ordinary fact that several kinds of evidence are discussed.
- Do not use as a generic synonym for mixed-methods synthesis.

**Boundary notes**
- Do not infer from heterogeneous evidence alone.
- Do not conflate with MixedMethodsSynthesis; an integrative review can use different synthesis methods.

**Positive examples**
- The authors explicitly state that the review was conducted as an integrative review design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports an integrative review design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.ScopingReviewDesign` — Scoping review design

**Depth:** `CORE_FACET`  
**Definition:** A review design explicitly conducted as a scoping review to map the extent, characteristics, concepts, or evidence landscape of a field.

**CODE WHEN**
- The publication explicitly identifies the work as a scoping review or follows a clearly stated scoping-review design.

**DO NOT CODE WHEN**
- Do not code ordinary broad reviews solely because they cover a wide topic.
- Do not equate scoping review with systematic mapping unless both are independently supported.

**Boundary notes**
- Do not treat broad topical scope as sufficient.
- ScopingReviewDesign and SystematicMappingDesign may look similar; use declared methodology/procedural framing, not output tables alone.

**Positive examples**
- The authors explicitly state that the review was conducted as a scoping review design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports a scoping review design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.SystematicMappingDesign` — Systematic mapping design

**Depth:** `CORE_FACET`  
**Definition:** A review design whose declared methodological purpose is systematic mapping/classification of a research area using an explicit systematic study-selection process.

**CODE WHEN**
- The publication explicitly declares a systematic mapping study/review or a mapping design with systematic search/selection procedures.

**DO NOT CODE WHEN**
- Do not infer merely from tables, taxonomies, or descriptive organization.
- A multivocal literature review is not automatically a systematic mapping design.

**Boundary notes**
- A taxonomy or evidence map output alone does not establish a systematic mapping design.
- A multivocal literature review is not automatically systematic mapping.

**Positive examples**
- The authors explicitly state that the review was conducted as a systematic mapping design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports a systematic mapping design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.SystematicReviewDesign` — Systematic review design

**Depth:** `CORE_FACET`  
**Definition:** A review design in which the publication frames the review itself as systematic and realizes that framing through an explicit, structured/reproducible evidence search or retrieval process plus explicit screening/selection/eligibility decisions for a bounded evidence set.

**CODE WHEN**
- The publication frames the review itself as a systematic review (or equivalent review-level systematic design) AND documents a structured/reproducible search or retrieval process AND explicit screening/selection/eligibility decisions for a bounded evidence set.

**DO NOT CODE WHEN**
- Do not code from the self-label “systematic review” alone when compatible structured search/retrieval and explicit selection/screening are not documented.
- Do not infer from systematic searching/retrieval alone when the paper does not frame the review/survey itself as systematic.
- Do not require quality appraisal as a universal condition for SystematicReviewDesign.

**Boundary notes**
- SystematicSurvey = evaluate SurveyFunction and SystematicReviewDesign separately.
- For SystematicReviewDesign, self-label is necessary/strong framing evidence but is not sufficient without compatible minimum process realization: structured search/retrieval + explicit selection/screening.

**Positive examples**
- The authors identify the publication as a systematic review and report structured database/search procedures plus explicit eligibility screening/selection of the evidence set.

**Negative examples**
- The paper calls itself a systematic review but does not document a structured search/retrieval procedure and explicit screening/selection.
- The paper performs a structured literature search but does not frame the review itself as systematic.

### `revmeta:hasReviewDesign.QualitativeEvidenceSynthesisDesign` — Qualitative evidence synthesis design

**Depth:** `CORE_FACET`  
**Definition:** A review design whose primary methodological design is synthesis of qualitative evidence or qualitative findings.

**CODE WHEN**
- The publication explicitly identifies qualitative evidence synthesis, qualitative systematic review, or an equivalent qualitative-synthesis design.

**DO NOT CODE WHEN**
- Do not code solely because the review contains qualitative discussion.
- Do not conflate with ThematicSynthesis, which is a synthesis method.

**Boundary notes**
- Do not infer from qualitative discussion alone.
- Distinguish design from ThematicSynthesis, QualitativeMetaSynthesis, or QualitativeContentAnalysis methods.

**Positive examples**
- The authors explicitly state that the review was conducted as a qualitative evidence synthesis design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports a qualitative evidence synthesis design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.RealistReviewDesign` — Realist review design

**Depth:** `CORE_FACET`  
**Definition:** A review design explicitly using realist review methodology to explain how and why outcomes arise in contexts through mechanisms or comparable realist constructs.

**CODE WHEN**
- The publication explicitly identifies itself as a realist review/synthesis design and applies realist explanatory logic.

**DO NOT CODE WHEN**
- Do not code merely because mechanisms or context are mentioned.
- Do not infer from causal discussion without realist methodology.

**Boundary notes**
- Require explicit realist methodology, not mere mention of mechanisms/context.
- RealistReviewDesign and RealistSynthesis can coexist but require independent design/method evidence.

**Positive examples**
- The authors explicitly state that the review was conducted as a realist review design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports a realist review design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.MetaNarrativeReviewDesign` — Meta-narrative review design

**Depth:** `CORE_FACET`  
**Definition:** A review design explicitly using meta-narrative methodology to examine how different research traditions have conceptualized and studied a topic.

**CODE WHEN**
- The publication explicitly identifies a meta-narrative review and analyzes research traditions or paradigmatic narratives.

**DO NOT CODE WHEN**
- Do not code ordinary historical review.
- Do not code merely because several disciplines are included.

**Boundary notes**
- Require explicit meta-narrative design and research-tradition logic.
- Distinguish from MetaNarrativeSynthesis, which is a synthesis-method assertion.

**Positive examples**
- The authors explicitly state that the review was conducted as a meta-narrative review design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports a meta-narrative review design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.UmbrellaReviewDesign` — Umbrella review design

**Depth:** `CORE_FACET`  
**Definition:** A review-of-reviews design in which existing systematic reviews or comparable secondary syntheses are the principal evidence units.

**CODE WHEN**
- The publication explicitly identifies an umbrella review/overview of reviews, or the design clearly appraises and synthesizes existing reviews as the main corpus.

**DO NOT CODE WHEN**
- Do not code merely because some reviews are cited.
- Do not add automatically to every meta-narrative review of reviews unless the umbrella role is independently supported.

**Boundary notes**
- Existing reviews must be the principal evidence units; citations to prior reviews are insufficient.
- Do not automatically add ExistingReview analytical object unless prior reviews are directly analyzed as objects under that property test.

**Positive examples**
- The authors explicitly state that the review was conducted as an umbrella review design, and the methods are compatible with that declared design.

**Negative examples**
- The publication never declares or substantively supports an umbrella review design; a superficially similar output or writing style is the only cue.

### `revmeta:hasReviewDesign.SystematizedReviewDesign` — Systematized review design

**Depth:** `CORE_FACET`  
**Definition:** A review design explicitly presented as systematized/systematised or semi-systematic: it deliberately applies substantial systematic-review elements while not claiming, or not meeting the publication’s own claim of, a full systematic review design.

**CODE WHEN**
- The publication explicitly self-identifies the design as systematized/systematised/semi-systematic review, OR explicitly states that it intentionally applies substantial systematic-review elements while presenting the design as partial/semi-systematic rather than a full systematic review.
- The declared partial/systematized design is reflected in the described review procedure.

**DO NOT CODE WHEN**
- Do not use as a fallback label for a systematic review that is incompletely reported, methodologically weak, or judged noncompliant.
- Do not infer solely from use of some systematic-search/screening practices without an explicit partial/systematized design cue.

**Boundary notes**
- SystematizedReviewDesign is a declared design family, not a quality grade.
- A single design claim should not be normalized simultaneously to SystematicReviewDesign and SystematizedReviewDesign; co-coding would require distinct independently reported design components.

**Positive examples**
- The methods explicitly describe a semi-systematic review that applies a structured search and screening process without claiming a full systematic review.

**Negative examples**
- A paper is missing several PRISMA items, but the authors still explicitly claim a systematic review; incompleteness alone does not make it systematized.

## revmeta:hasPublicationFunction — publication function

**Tier:** `CORE_FACET`  
**Definition:** Relates a review publication to a principal communicative or scholarly function that is explicitly cued and materially realized in the publication.

**Boundary:** The same publication may realize several functions. Distinguish function from design, contribution claim, and output artifact.

### `revmeta:hasPublicationFunction.SurveyFunction` — Survey function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that explicitly presents the article as a survey or field-organizing survey and materially realizes that role.

**CODE WHEN**
- The publication self-identifies as a survey in title, abstract, metadata, introduction or comparable central text and materially organizes/synthesizes a field.

**DO NOT CODE WHEN**
- Generic 'overview' or 'comprehensive overview' wording alone is insufficient.
- Do not infer solely from being a systematic/scoping/umbrella review.

**Boundary notes**
- A statement that the work is not a “systematic survey” does not negate SurveyFunction; function and design are separate.

**Positive examples**
- The abstract/objective explicitly gives the publication a survey function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling survey function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.StateOfTheArtFunction` — State-of-the-art function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function whose explicit objective is to characterize the current state, current landscape, or current research frontier of a field at a defined time and which materially realizes that temporal/current-state characterization.

**CODE WHEN**
- The publication explicitly frames a principal objective/function as characterizing the current state, state of the art, current landscape, frontier, or equivalent present-time status of a field.
- The paper materially realizes this by synthesizing what is currently established, dominant, emerging, limited, or open at the stated time.

**DO NOT CODE WHEN**
- Do not infer from “state-of-the-art/SOTA” modifying methods/approaches/models; the cue must characterize the publication’s own objective/function.
- Do not infer from recency alone.

**Boundary notes**
- “Current methods/frameworks” or “how X is currently assessed” can establish paper-level current-state function when this is an explicit objective and materially synthesized.

**Positive examples**
- The abstract/objective explicitly gives the publication a state-of-the-art function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling state-of-the-art function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.CriticalSynthesisFunction` — Critical synthesis function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function explicitly aimed at interpretive critique of assumptions, contradictions, limitations, validity, paradigms, or applicability across the literature.

**CODE WHEN**
- A central objective explicitly frames the work as critical examination/synthesis and the paper materially critiques assumptions, reporting, contradictions, limitations, validity or applicability across the literature.

**DO NOT CODE WHEN**
- The adjective “critical” without sustained critique is insufficient; routine limitations or quality scoring alone remain insufficient.

**Boundary notes**
- Risk-of-bias scoring alone is not critical synthesis.
- Ordinary limitations discussion is insufficient; critique must be a principal function.

**Positive examples**
- The abstract/objective explicitly gives the publication a critical synthesis function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling critical synthesis function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.TutorialFunction` — Tutorial function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that explicitly teaches or explains a field, method, or body of concepts to enable reader understanding or practice.

**CODE WHEN**
- The source explicitly frames the article as a tutorial/primer/educational guide and materially explains concepts or procedures.

**DO NOT CODE WHEN**
- Do not infer from background explanations that are normal parts of any review.

**Boundary notes**
- Background explanation common to reviews is insufficient.
- Require an explicit educational/tutorial role plus material teaching content.

**Positive examples**
- The abstract/objective explicitly gives the publication a tutorial function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling tutorial function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.PositionFunction` — Position function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that explicitly advances or defends a scholarly position, stance, or normative claim.

**CODE WHEN**
- The paper explicitly frames a position/stance and develops arguments supporting it.

**DO NOT CODE WHEN**
- Do not code ordinary conclusions or recommendations as a position function.

**Boundary notes**
- Distinguish from PerspectiveFunction: position defends/advances a substantive stance; perspective may offer interpretation without advocating a proposition.

**Positive examples**
- The abstract/objective explicitly gives the publication a position function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling position function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.PerspectiveFunction` — Perspective function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that explicitly offers a perspective or interpretive viewpoint on a field rather than only summarizing evidence.

**CODE WHEN**
- The source explicitly identifies the article as a perspective or states that its purpose is to offer an interpretive perspective.

**DO NOT CODE WHEN**
- Do not infer from ordinary author interpretation in Discussion.

**Boundary notes**
- Distinguish from PositionFunction; ordinary author interpretation is insufficient.

**Positive examples**
- The abstract/objective explicitly gives the publication a perspective function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling perspective function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.VisionFunction` — Vision function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that explicitly articulates a desired or anticipated future state, architecture, principles, or development trajectory for a field and substantively develops that future-oriented view.

**CODE WHEN**
- The publication explicitly presents a principal future-oriented vision, target state, architecture, set of principles, or development trajectory for the field/system.
- That future state/trajectory is materially developed beyond generic implications or future-work remarks.

**DO NOT CODE WHEN**
- Do not infer from generic future-work paragraphs or isolated predictions.
- Do not code merely because the paper proposes research questions or priorities; those support AgendaSettingFunction unless a distinct future target state/trajectory is also articulated.

**Boundary notes**
- A vision specifies a future target state/trajectory; an agenda structures research work to pursue.
- VisionFunction and AgendaSettingFunction may coexist when independently explicit.

**Positive examples**
- The abstract/objective explicitly gives the publication a vision function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling vision function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.AgendaSettingFunction` — Agenda-setting function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that explicitly structures, prioritizes, or formulates multiple future research directions or questions as a major purpose of the publication.

**CODE WHEN**
- A paper-level cue or substantial dedicated section organizes multiple future research directions/questions/challenges/priorities as a material function.

**DO NOT CODE WHEN**
- Brief routine future-work/open-problem prose is insufficient even if mentioned in the abstract.

**Boundary notes**
- A substantial dedicated Challenges/Future Directions section can establish function; principality is materiality-based, not restricted to being the sole objective.

**Positive examples**
- The abstract/objective explicitly gives the publication an agenda-setting function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling agenda-setting function, but no principal function cue and material realization are both present.

### `revmeta:hasPublicationFunction.ProtocolFunction` — Protocol function

**Depth:** `CORE_FACET`  
**Definition:** A principal publication function that presents the planned methods or protocol for a review or synthesis before or independently of reporting completed review findings.

**CODE WHEN**
- The publication explicitly identifies itself as a review protocol or its main purpose is to specify a planned review procedure.

**DO NOT CODE WHEN**
- Do not code a completed review merely because it cites or summarizes its protocol.

**Boundary notes**
- A completed review is not a protocol merely because it references a prior protocol.
- Code dual function only if the same publication materially serves both protocol and completed-report roles.

**Positive examples**
- The abstract/objective explicitly gives the publication a protocol function role and a substantial section or output realizes that role.

**Negative examples**
- The paper contains incidental material resembling protocol function, but no principal function cue and material realization are both present.

## revmeta:hasEvidenceSourceRole — evidence source role

**Tier:** `CORE_FACET`  
**Definition:** Relates the review to semantic roles played by sources that materially contribute analyzable evidence to the included corpus, including primary/secondary/survey/practice-based evidence and methodological-guidance evidence.

**Boundary:** Source roles may coexist. MethodologicalGuidanceSource is role-based, not a document type: a Guideline/Standard/JournalArticle can bear this role, and a methodological empirical study can additionally be PrimaryStudyReport if both roles are material.

### `revmeta:hasEvidenceSourceRole.PrimaryStudyReport` — Primary study report

**Depth:** `CORE_FACET`  
**Definition:** An included source whose semantic role is to report original primary research that contributes analyzable evidence to the review.

**CODE WHEN**
- Original primary research reports materially supply evidence that is synthesized, categorized, compared, or interpreted in the main analysis. A formal included-study table is helpful but not required for narrative surveys when the role is clear from substantive analysis.

**DO NOT CODE WHEN**
- Do not infer from isolated/background primary-study citations or document format alone.

**Boundary notes**
- Document type does not determine primary-study role.
- Code only if primary reports materially contribute analyzable evidence.

**Positive examples**
- The included-corpus description and synthesis show that primary study report sources materially contribute analyzable evidence.

**Negative examples**
- Primary study report sources are mentioned in background/search eligibility but are not shown to contribute analyzable evidence to the final corpus.

### `revmeta:hasEvidenceSourceRole.SecondaryStudyReport` — Secondary study report

**Depth:** `CORE_FACET`  
**Definition:** An included source whose semantic role is to report a prior secondary synthesis such as a review or meta-analysis.

**CODE WHEN**
- Prior reviews/meta-analyses/secondary syntheses materially supply evidence used in the review’s analysis/results, whether or not they are the sole corpus type.

**DO NOT CODE WHEN**
- Do not code reviews cited only for background/positioning.

**Boundary notes**
- Do not infer from a paper being called a review unless it is included as evidence.
- ExistingSurvey is not automatically co-coded; apply each role definition independently.

**Positive examples**
- The included-corpus description and synthesis show that secondary study report sources materially contribute analyzable evidence.

**Negative examples**
- Secondary study report sources are mentioned in background/search eligibility but are not shown to contribute analyzable evidence to the final corpus.

### `revmeta:hasEvidenceSourceRole.ExistingSurvey` — Existing survey

**Depth:** `CORE_FACET`  
**Definition:** An included source whose semantic role is an existing survey publication that is itself analyzed by the current review/survey.

**CODE WHEN**
- Existing survey papers are included as analyzable evidence units.

**DO NOT CODE WHEN**
- Do not code the current paper's own SurveyFunction here.
- Do not infer from references to surveys in background.

**Boundary notes**
- An included survey publication is substantively used as evidence.
- Do not automatically treat it as SecondaryStudyReport; co-code only when the survey also satisfies that role.

**Positive examples**
- The included-corpus description and synthesis show that existing survey sources materially contribute analyzable evidence.

**Negative examples**
- Existing survey sources are mentioned in background/search eligibility but are not shown to contribute analyzable evidence to the final corpus.

### `revmeta:hasEvidenceSourceRole.PracticeBasedSource` — Practice-based source

**Depth:** `CORE_FACET`  
**Definition:** An included source whose evidential role is to contribute practitioner, professional, operational, organizational, policy/practice, or other practice-origin knowledge/data substantively to the synthesis, regardless of document format.

**CODE WHEN**
- Institutional, organizational, government, professional or practitioner-origin sources contribute substantive operational/practice/policy evidence or data used in synthesis.

**DO NOT CODE WHEN**
- Do not classify methodological guidance as practice-based solely because it gives recommendations.
- Document type or grey-literature status alone is insufficient.

**Boundary notes**
- Organizational/government reports can qualify when they materially provide operational/practice/policy evidence. Methodological-guidance role remains a vocabulary-gap candidate.

**Positive examples**
- The included-corpus description and synthesis show that practice-based source sources materially contribute analyzable evidence.

**Negative examples**
- Practice-based source sources are mentioned in background/search eligibility but are not shown to contribute analyzable evidence to the final corpus.

### `revmeta:hasEvidenceSourceRole.MethodologicalGuidanceSource` — Methodological guidance source

**Depth:** `CORE_FACET`  
**Definition:** An included source whose evidential role is to provide methodological knowledge, guidance, recommendations, reporting/conduct guidance, or method-focused evidence about how research, reviews, evidence synthesis, appraisal, measurement, or reporting should be designed or performed, where that methodological content materially contributes to the review synthesis.

**CODE WHEN**
- Guidance documents, methodological recommendations, methodological studies, reporting/conduct guidance, or comparable method-focused sources materially contribute methodological evidence that is synthesized, compared, mapped, appraised, or interpreted.
- A methodological empirical study may also be PrimaryStudyReport when it reports original research; code each material role independently.

**DO NOT CODE WHEN**
- Do not code domain-practice/policy guidance as methodological guidance when its role is operational or clinical/professional practice; evaluate PracticeBasedSource instead.
- Do not infer from document type alone: a Guideline or Standard document is not automatically a MethodologicalGuidanceSource.
- Do not code methodological guidance cited only as the current review’s own procedural authority unless it is itself part of the analyzed evidence corpus.

**Boundary notes**
- This is an evidence-source role, not a document type. It is independent of Guideline, Standard, JournalArticle, TechnicalReport, etc.
- It can co-occur with PrimaryStudyReport or SecondaryStudyReport when the same included source materially bears both roles.
- This development-only term closes a vocabulary gap observed in v0.2.1 source adjudication and independently replicated in the fresh v0.2.2 held-out set (RT-H05).

**Positive examples**
- A scoping review synthesizes reporting recommendations and methodological guidance studies to compare how mapping reviews should be conducted and reported.
- A review analyzes methodological papers and guidance documents about automation or evidence-synthesis methods as evidence units.

**Negative examples**
- The authors state that they followed PRISMA or Cochrane guidance, but those documents are not analyzed as evidence.
- A clinical guideline is included for its practice recommendations rather than methodological guidance; evaluate PracticeBasedSource and document type independently.

## revmeta:hasSourceDocumentType — source document type

**Tier:** `OPTIONAL_DETAIL`  
**Definition:** Relates the review to document or publication types demonstrably present in the included analyzable corpus.

**Boundary:** Documentary forms are independent of evidence roles and corpus-composition boundedness. Do not import the stronger bounded-final-corpus threshold from hasCorpusComposition into source-document presence decisions.

### `revmeta:hasSourceDocumentType.JournalArticle` — Journal article

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A scholarly article published in a journal.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a journal article, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included journal article.

**Negative examples**
- The protocol says that journal article sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.ConferencePaper` — Conference paper

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A paper published in or as part of a scholarly conference/proceedings venue.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a conference paper, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included conference paper.

**Negative examples**
- The protocol says that conference paper sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.Preprint` — Preprint

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A manuscript publicly disseminated before or without formal version-of-record publication.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a preprint, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- Code the version actually included; do not automatically add JournalArticle for a later version of the same work.
- For corpus composition, RevMeta operationally treats scholarly preprints as academic literature unless contrary corpus logic is explicit.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included preprint.

**Negative examples**
- The protocol says that preprint sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.Thesis` — Thesis

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A dissertation or thesis submitted for an academic degree.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a thesis, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included thesis.

**Negative examples**
- The protocol says that thesis sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.TechnicalReport` — Technical report

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A formal technical or research report issued outside ordinary journal/conference publication.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a technical report, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- Distinguish from WhitePaper by purpose/provenance: technical/research reporting versus advocacy/authoritative explanatory document.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included technical report.

**Negative examples**
- The protocol says that technical report sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.WhitePaper` — White paper

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** An authoritative or policy/industry-oriented white paper used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a white paper, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- Distinguish from TechnicalReport; use source self-identification and purpose rather than publisher type alone.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included white paper.

**Negative examples**
- The protocol says that white paper sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.Guideline` — Guideline

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A formal guideline or recommendations document used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a guideline, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- A guideline gives recommendations for practice/policy; a Standard sets normative technical/professional requirements.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included guideline.

**Negative examples**
- The protocol says that guideline sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.EditorialCommentary` — Editorial or commentary

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** An editorial, commentary, viewpoint, or comparable short opinion/interpretive publication used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be an editorial or commentary, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- Distinguish formal editorial/commentary publication from informal BlogPost or generic perspective article.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included editorial or commentary.

**Negative examples**
- The protocol says that editorial or commentary sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.BlogPost` — Blog post

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A blog or web-post publication used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a blog post, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- A web page is not automatically a blog post; use publication form and provenance.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included blog post.

**Negative examples**
- The protocol says that blog post sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.BookOrChapter` — Book or chapter

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A book or book chapter used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a book or chapter, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included book or chapter.

**Negative examples**
- The protocol says that book or chapter sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.Documentation` — Documentation

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** Technical, software, platform, API, or other formal documentation used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be documentation, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- Distinguish technical/software/API documentation from ProgrammeManual and from general web pages.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included documentation.

**Negative examples**
- The protocol says that documentation sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.Standard` — Standard

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A formal technical, professional, or regulatory standard used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a standard, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- This is the documentary form of an included standards publication.
- Do not confuse with revmeta:hasAnalyticalObjectType.Standard, which asks whether standards are themselves analyzed.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included standard.

**Negative examples**
- The protocol says that standard sources were eligible, but the final corpus does not demonstrate that any were included.

### `revmeta:hasSourceDocumentType.ProgrammeManual` — Programme manual

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A manual describing the operation, delivery, or procedures of a programme/intervention used as an included source.

**CODE WHEN**
- At least one included analyzable source is demonstrated to be a programme manual, or a mandatory restrictive criterion establishes that all included sources are of this type.

**DO NOT CODE WHEN**
- An allowed/eligible-type list alone is insufficient.
- Search scope alone is insufficient.
- Reference-list formatting alone is insufficient.

**Boundary notes**
- Distinguish operational programme/intervention manual from general Documentation or Guideline.

**Positive examples**
- The final included-corpus table or text demonstrates at least one included programme manual.

**Negative examples**
- The protocol says that programme manual sources were eligible, but the final corpus does not demonstrate that any were included.

## revmeta:hasAnalyticalObjectType — analytical object type

**Tier:** `CORE_FACET`  
**Definition:** Relates the review to broad categories that themselves function as material analytical dimensions or direct targets of cross-corpus comparison, classification, mapping, appraisal, aggregation, interpretation, or synthesis. Mere evidence-carrier status, routine extraction, evaluation context, or named-instance occurrence is insufficient.

**Boundary:** Multi-label coexistence is allowed only when each neighbor has independent material evidence. Do not co-code broader/adjacent terms merely because one concrete object can be described in several everyday-language ways.

### `revmeta:hasAnalyticalObjectType.Study` — Study

**Depth:** `CORE_FACET`  
**Definition:** A primary study treated as an analytical carrier/object whose study-level design, setting, quality, methodology, population, distribution, or other study-level characteristics are themselves materially synthesized.

**CODE WHEN**
- Study-level characteristics or quality/design distributions are systematically compared, mapped, appraised, or synthesized.

**DO NOT CODE WHEN**
- Do not code Study merely because primary studies are the evidence sources or because their findings are synthesized.

**Boundary notes**
- Evidence-source role PrimaryStudyReport does not entail analytical-object Study.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes study objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Study appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.EffectEstimate` — Effect estimate

**Depth:** `CORE_FACET`  
**Definition:** A quantitative effect/performance estimate or comparable normalized quantitative result that is itself extracted, compared, or aggregated across sources.

**CODE WHEN**
- Effect sizes, odds/risk ratios, standardized effects, or directly comparable normalized performance deltas are synthesized across sources.

**DO NOT CODE WHEN**
- Do not code simple raw metrics/counts that are not treated as comparable effect/performance estimates across sources.

**Boundary notes**
- Operational scope is cross-domain in v0.2.2: comparable computational performance deltas may qualify when functioning analogously to effect estimates.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes effect estimate objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Effect estimate appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.ExistingReview` — Existing review

**Depth:** `CORE_FACET`  
**Definition:** A prior review publication whose review-level design, scope, quality, methods, coverage, or conclusions are themselves materially compared/appraised/mapped as review objects.

**CODE WHEN**
- Existing reviews are direct units of review-level comparison/appraisal/synthesis.

**DO NOT CODE WHEN**
- Do not code merely because prior reviews are evidence carriers or citations.

**Boundary notes**
- EvidenceSourceRole SecondaryStudyReport does not entail AnalyticalObjectType ExistingReview.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes existing review objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Existing review appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.ExistingSurvey` — Existing survey

**Depth:** `CORE_FACET`  
**Definition:** A prior survey publication whose survey-level scope, organization, coverage, methods, or features are directly compared, classified, appraised, or synthesized.

**CODE WHEN**
- Prior surveys are explicitly treated as survey objects, for example in a comparative matrix of survey features.

**DO NOT CODE WHEN**
- Do not code surveys discussed only in Related Work or used as background evidence.

**Boundary notes**
- EvidenceSourceRole ExistingSurvey does not entail AnalyticalObjectType ExistingSurvey.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes existing survey objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Existing survey appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.ResearchMethod` — Research method

**Depth:** `CORE_FACET`  
**Definition:** A method for conducting research, evaluation, measurement, evidence synthesis, or empirical investigation that is itself materially compared, classified, appraised, or synthesized. It does not include domain technical/computational techniques merely because authors call them methods or approaches.

**CODE WHEN**
- Research/evaluation/investigation methods themselves are compared, categorized, appraised, or synthesized across sources.
- Examples include study designs, statistical/analytical methods, evaluation methodologies, qualitative/quantitative research procedures, or evidence-synthesis methods when they are objects of the review rather than methods used by the current review.

**DO NOT CODE WHEN**
- Do not code domain techniques for solving the subject-matter task (e.g., prompting, retrieval, fine-tuning, ranking, reasoning, generation pipelines) merely because the source calls them methods/approaches.
- Do not code the current review’s own synthesis method here; use usesSynthesisMethod.

**Boundary notes**
- ResearchMethod answers “how was research/evaluation/investigation conducted?”. Technical computational procedures answering “how does the system solve the domain task?” belong under Algorithm/ComputationalModel/Architecture as appropriate.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes research method objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Research method appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.ComputationalModel` — Computational model

**Depth:** `CORE_FACET`  
**Definition:** A computational or machine-learning model family or model instance treated as a material object of comparison, characterization, or synthesis.

**CODE WHEN**
- Models are directly compared/classified/evaluated as objects.

**DO NOT CODE WHEN**
- Do not code when model type is only a routine attribute used to classify studies.

**Boundary notes**
- Distinguish model/model family from Algorithm (procedure) and Architecture (structural organization).
- Named model instances remain entity-extension data; the RevMeta core assertion is the broad object category.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes computational model objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Computational model appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Algorithm` — Algorithm

**Depth:** `CORE_FACET`  
**Definition:** A computational or technical procedure, technique, strategy, or algorithmic approach for transforming inputs or solving a domain task that is itself materially compared, classified, evaluated, or synthesized.

**CODE WHEN**
- Computational/technical techniques or procedure families are direct analytical dimensions, including retrieval, ranking, prompting, fine-tuning, reasoning, search, optimization, generation, or comparable algorithmic strategies when materially synthesized.

**DO NOT CODE WHEN**
- Do not code research-study designs, statistical analysis methods, or evaluation/review methodology; those are ResearchMethod.
- Do not code a named algorithm mentioned only as an implementation detail or example.

**Boundary notes**
- The preferred label remains Algorithm for vocabulary stability, but operational scope includes materially analyzed computational/technical technique families. This is a label clarification, not a new class.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes algorithm objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Algorithm appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Architecture` — Architecture

**Depth:** `CORE_FACET`  
**Definition:** A system, software, model, or technical architecture treated as a material object of comparison, classification, or synthesis.

**CODE WHEN**
- Architectures themselves are compared/categorized or their structural trade-offs are synthesized.

**DO NOT CODE WHEN**
- Do not code when 'architecture' is merely an attribute value assigned to studies.

**Boundary notes**
- Distinguish system/model structure from algorithm and from DesignArtifact output created by the review.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes architecture objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Architecture appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Dataset` — Dataset

**Depth:** `CORE_FACET`  
**Definition:** A data collection/corpus whose dataset-level types, properties, availability, distribution, composition, limitations, or use patterns are themselves materially synthesized.

**CODE WHEN**
- Datasets are systematically categorized, compared, counted, characterized, or evaluated at dataset level across the corpus.

**DO NOT CODE WHEN**
- Do not code when a dataset merely identifies where another object (model/algorithm/framework) was evaluated.
- Do not infer Dataset solely because benchmark tables list dataset names.

**Boundary notes**
- Dataset and Benchmark may co-occur only when dataset characteristics are independently synthesized in addition to benchmark role.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes dataset objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Dataset appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Benchmark` — Benchmark

**Depth:** `CORE_FACET`  
**Definition:** A benchmark, benchmark suite/task, or dataset functioning as an evaluative reference whose benchmark role, coverage, design, usage, or comparative properties are themselves materially synthesized.

**CODE WHEN**
- Benchmarks are compared, categorized, counted/interpreted across the corpus, or analyzed as evaluative references.

**DO NOT CODE WHEN**
- Do not code merely because papers report evaluation on named datasets or because generic benchmarking occurs.

**Boundary notes**
- A dataset can be Benchmark without Dataset if only its evaluative-reference role is analyzed; co-code Dataset only for independent dataset-level analysis.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes benchmark objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Benchmark appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Framework` — Framework

**Depth:** `CORE_FACET`  
**Definition:** A conceptual, methodological, evaluative, or organizational framework from the reviewed domain that is itself materially compared, classified, mapped, or appraised as an organizing structure.

**CODE WHEN**
- Framework structures/components/relations/rules are direct analytical objects.

**DO NOT CODE WHEN**
- Do not code executable software merely called a framework; evaluate SoftwareTool.
- Do not code a framework produced only by the current review; use producesOutputArtifact unless prior frameworks are also analyzed.

**Boundary notes**
- Framework denotes organizing structure; SoftwareTool denotes executable/operational software. Co-code only for distinct material roles.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes framework objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Framework appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.SoftwareTool` — Software tool

**Depth:** `CORE_FACET`  
**Definition:** Executable software, toolkit, library, platform, package, application, or operational software framework that is itself materially compared, classified, evaluated, or synthesized.

**CODE WHEN**
- Tools/toolkits/platforms are direct review objects and their capabilities, availability, features, use, or performance are synthesized.

**DO NOT CODE WHEN**
- Do not code software mentioned only in background or used administratively by included studies.
- Do not code a conceptual/evaluative framework merely because it is called a framework.

**Boundary notes**
- Executable/operational implementation favors SoftwareTool; abstract organizing structure favors Framework.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes software tool objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Software tool appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.ResearchTradition` — Research tradition

**Depth:** `CORE_FACET`  
**Definition:** A distinct research tradition, paradigm, school, or lineage that is itself compared or synthesized.

**CODE WHEN**
- Research traditions/paradigms are explicit units of analysis.

**DO NOT CODE WHEN**
- Do not infer merely because included studies come from multiple disciplines.

**Boundary notes**
- A discipline label alone is insufficient; the tradition/paradigm must itself be compared or synthesized.
- Particularly relevant to meta-narrative work but not implied by that label alone.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes research tradition objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Research tradition appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.BibliographicMetadata` — Bibliographic metadata

**Depth:** `CORE_FACET`  
**Definition:** Publication-level metadata (for example year, venue, authorship, citation, keyword, affiliation, or publication counts) that are materially aggregated, modeled, compared, or interpreted across the corpus.

**CODE WHEN**
- Metadata are aggregated/interpreted for trends, distributions, citation/bibliometric/network analysis, or comparable synthesis.

**DO NOT CODE WHEN**
- Routine extraction of author/year/venue alone is insufficient.

**Boundary notes**
- Routine extraction of year/author/venue is insufficient.
- Simple descriptive counts may support this object type without necessarily supporting BibliometricNetworkSynthesis as a method.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes bibliographic metadata objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Bibliographic metadata appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Concept` — Concept

**Depth:** `CORE_FACET`  
**Definition:** A concept, construct, term, or definition that is itself compared, synthesized, clarified, or organized.

**CODE WHEN**
- Concepts/definitions are direct targets of synthesis or comparison.

**DO NOT CODE WHEN**
- Do not code every topic word or construct merely mentioned.

**Boundary notes**
- Distinguish concept/construct/definition from Theory (explanatory system) and Framework (organizing structure).

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes concept objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Concept appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Theory` — Theory

**Depth:** `CORE_FACET`  
**Definition:** A theory or theoretical model that is itself compared, evaluated, synthesized, or mapped.

**CODE WHEN**
- Theories themselves are direct analytical targets.

**DO NOT CODE WHEN**
- Do not code when theory is only a study characteristic or background reference.

**Boundary notes**
- A theory cited as a study characteristic is insufficient; theories must themselves be compared/evaluated/synthesized.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes theory objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Theory appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Finding` — Finding

**Depth:** `CORE_FACET`  
**Definition:** A propositional result, conclusion, qualitative theme, interpretation, or source-level finding that is itself compared/integrated across sources as finding content.

**CODE WHEN**
- Source findings/themes/conclusions are directly synthesized across sources.

**DO NOT CODE WHEN**
- Do not code routine extraction of study results without finding-level synthesis.
- Do not automatically co-code Finding when the specific analytical object is an EffectEstimate.
- Do not treat the current review’s own conclusion as an included-source Finding.

**Boundary notes**
- Finding is content-level synthesis; EffectEstimate is a specific quantitative result object. Co-code only when both forms are independently synthesized.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes finding objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Finding appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.InterventionOrProgramme` — Intervention or programme

**Depth:** `CORE_FACET`  
**Definition:** An intervention, service, programme, policy implementation, or organized practice intervention that is itself compared, characterized, evaluated, or synthesized.

**CODE WHEN**
- Interventions/programmes are direct synthesis targets.

**DO NOT CODE WHEN**
- Do not code when intervention is only a study-level eligibility attribute without material synthesis.

**Boundary notes**
- Prefer InterventionOrProgramme when the analyzed object is a deliberately delivered/implemented intervention, programme, service or exposure configuration with components/timing. Do not additionally code Practice unless professional/operational practice itself is independently synthesized.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes intervention or programme objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Intervention or programme appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Mechanism` — Mechanism

**Depth:** `CORE_FACET`  
**Definition:** A causal, explanatory, behavioral, organizational, or realist mechanism that is itself analyzed or synthesized.

**CODE WHEN**
- Mechanisms are explicitly compared, inferred, or synthesized as explanatory objects.

**DO NOT CODE WHEN**
- Do not code ordinary causal language without mechanisms as analytical targets.

**Boundary notes**
- Require mechanisms themselves to be analyzed/synthesized, not merely mentioned as causal language.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes mechanism objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Mechanism appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Repository` — Repository

**Depth:** `CORE_FACET`  
**Definition:** A repository, archive, registry, or comparable collection service that is itself compared, characterized, or evaluated.

**CODE WHEN**
- Repositories/registries are direct objects of review analysis.

**DO NOT CODE WHEN**
- Do not code a repository merely because it hosts supplementary material.

**Boundary notes**
- Distinguish repository/archive/registry service from Dataset (content) and ResearchResource produced by the current review.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes repository objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Repository appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Taxonomy` — Taxonomy

**Depth:** `CORE_FACET`  
**Definition:** A taxonomy or classification scheme from the reviewed literature that is itself compared, evaluated, mapped, or synthesized.

**CODE WHEN**
- Existing taxonomies are analytical objects.

**DO NOT CODE WHEN**
- Do not code a taxonomy produced by the current review as an AnalyticalObject unless prior taxonomies are also being analyzed; use TaxonomyArtifact for the produced output.

**Boundary notes**
- Distinguish taxonomies found in prior literature from TaxonomyArtifact produced by the current review.
- Taxonomy primarily classifies; Framework generally organizes relationships/processes beyond classification.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes taxonomy objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Taxonomy appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Practice` — Practice

**Depth:** `CORE_FACET`  
**Definition:** A professional, organizational, engineering, clinical, or operational practice that is itself compared, classified, or synthesized.

**CODE WHEN**
- Practices are direct analytical targets.

**DO NOT CODE WHEN**
- Do not code merely because practitioners are study participants.

**Boundary notes**
- Practice is a recurring professional/organizational/clinical/engineering way of working. If the object is a deliberately delivered intervention/programme with defined components/timing, prefer InterventionOrProgramme unless practice itself is independently analyzed.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes practice objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Practice appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Indicator` — Indicator

**Depth:** `CORE_FACET`  
**Definition:** A metric, indicator, criterion, index, score, or other operational quantity/dimension that is itself materially compared, categorized, evaluated, or synthesized across the reviewed corpus.

**CODE WHEN**
- Metrics/indicators are direct analytical targets.

**DO NOT CODE WHEN**
- Do not code every numeric variable extracted from a study.

**Boundary notes**
- An indicator/metric/criterion is a measured quantity or evaluative dimension; MeasurementInstrument is the tool/procedure used to obtain measurements.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes indicator objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Indicator appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.MeasurementInstrument` — Measurement instrument

**Depth:** `CORE_FACET`  
**Definition:** A scale, questionnaire, rubric, rating system, assessment instrument, or other structured instrument used to generate measurements and itself materially compared, appraised, or synthesized.

**CODE WHEN**
- Measurement instruments are direct objects of appraisal/comparison.

**DO NOT CODE WHEN**
- Do not code an instrument merely because a study used it.

**Boundary notes**
- Distinguish scales/questionnaires/instruments from the indicators/metrics they operationalize.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes measurement instrument objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Measurement instrument appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

### `revmeta:hasAnalyticalObjectType.Standard` — Standard

**Depth:** `CORE_FACET`  
**Definition:** A technical, methodological, professional, reporting, or regulatory standard whose requirements/content/structure are themselves materially compared, mapped, appraised, or synthesized.

**CODE WHEN**
- Standards are direct analytical reference objects, for example findings are systematically mapped against their requirements or standards are compared.

**DO NOT CODE WHEN**
- Do not code a standard merely because the current review follows, cites, or reports compliance with it.

**Boundary notes**
- Standard-as-methodological-guidance-used-by-review is not Standard-as-analytical-object.

**Positive examples**
- The review directly compares, classifies, appraises, or synthesizes standard objects across the corpus as a substantive part of the analysis.

**Negative examples**
- Standard appears only as a routine study attribute, implementation detail, or isolated example and is not itself synthesized.

## revmeta:hasCorpusComposition — corpus composition

**Tier:** `CORE_FACET`  
**Definition:** Classifies the included analyzable evidence corpus by whether it consists of scholarly/academic literature, grey/practice literature, or a substantive combination of both.

**Boundary:** AcademicLiteratureCorpus, GreyLiteratureCorpus, and AcademicAndGreyLiteratureCorpus are mutually exclusive.

### `revmeta:hasCorpusComposition.AcademicLiteratureCorpus` — Academic literature corpus

**Depth:** `CORE_FACET`  
**Definition:** An evidence corpus composed of academic/scholarly literature under the review's inclusion and analysis rules.

**CODE WHEN**
- A sufficiently bounded final analyzable corpus is demonstrated to consist of scholarly/academic literature, with no materially included grey/practice component.

**DO NOT CODE WHEN**
- Do not infer academic-only composition from scholarly tone, academic citations, database use, or lack of explicit grey-literature mention in an unbounded narrative survey.

**Boundary notes**
- Operationally includes scholarly preprints for RevMeta consistency.
- Do not infer academic-only composition if practice/grey sources materially enter analysis.

**Positive examples**
- All analyzable included sources are scholarly research publications/preprints and no substantive grey/practice sources enter the synthesis.

**Negative examples**
- The search included reports and practitioner material, and some of those sources enter the analysis; the corpus is not academic-only.

### `revmeta:hasCorpusComposition.GreyLiteratureCorpus` — Grey literature corpus

**Depth:** `CORE_FACET`  
**Definition:** An evidence corpus composed of grey/practice/non-formally-published literature under the review's inclusion and analysis rules.

**CODE WHEN**
- Included analyzable sources are substantively grey/practice/non-formal literature without an academic-literature component.

**DO NOT CODE WHEN**
- Do not infer merely because grey-literature sources were searched but none were included.

**Boundary notes**
- Use only when the analyzable corpus is composed of grey/practice/non-conventional scholarly-publication sources.
- Searches of grey literature without included grey sources are insufficient.

**Positive examples**
- The analyzable corpus consists of practice/technical/policy or other grey sources rather than scholarly research literature.

**Negative examples**
- Grey-literature websites were searched, but the included analyzable corpus contains only scholarly papers.

### `revmeta:hasCorpusComposition.AcademicAndGreyLiteratureCorpus` — Academic and grey literature corpus

**Depth:** `CORE_FACET`  
**Definition:** An evidence corpus containing both academic literature and substantively included grey/practice literature.

**CODE WHEN**
- Both academic and grey/practice sources enter the included analyzable corpus.

**DO NOT CODE WHEN**
- Searching grey literature without including it is insufficient.

**Boundary notes**
- Requires substantive included sources from both categories.
- It is not triggered merely by broad eligibility or search scope.

**Positive examples**
- The final analyzable corpus contains both scholarly research publications and substantively included grey/practice sources.

**Negative examples**
- Both academic and grey sources were eligible, but only academic sources appear in the final analyzed corpus.

## revmeta:usesSynthesisMethod — synthesis method

**Tier:** `CORE_FACET`  
**Definition:** Relates the review to substantive methods used to integrate, aggregate, code, map, interpret, or otherwise synthesize evidence across included sources.

**Boundary:** Explicit label plus substantive realization is sufficient; label alone is not. Nested synthesis methods may coexist. Local framework use, presentation style, and extraction are not independent synthesis methods.

### `revmeta:usesSynthesisMethod.NarrativeSynthesis` — Narrative synthesis

**Depth:** `CORE_FACET`  
**Definition:** A substantive synthesis method that integrates evidence across sources through a deliberate narrative procedure. An explicit narrative-synthesis statement plus a described cross-source organization/integration step is sufficient; narrative prose alone is not.

**CODE WHEN**
- The source explicitly reports narrative synthesis in a synthesis/analysis context and describes cross-source integration/organization; OR an identifiable narrative-synthesis procedure is described without the label.

**DO NOT CODE WHEN**
- Do not code ordinary narrative reporting or discussion prose without cross-source integration.
- Do not reject a substantive narrative-synthesis stage merely because it is nested within thematic/framework/meta-synthesis.

**Boundary notes**
- Nested coexistence is allowed. The minimum positive evidence is explicit method cue + substantive cross-source realization, not a full textbook protocol.

**Positive examples**
- The methods/results show narrative synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling narrative synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.DescriptiveMappingSynthesis` — Descriptive mapping synthesis

**Depth:** `CORE_FACET`  
**Definition:** A substantive synthesis method that systematically maps the included evidence across explicit categories, dimensions, or cells and interprets corpus-level distributions, patterns, concentrations, or gaps produced by that mapping.

**CODE WHEN**
- Gate 1 — mapping structure: the review defines or derives explicit categories, dimensions, cells, or comparable variables for mapping the evidence.
- Gate 2 — corpus application: included evidence is systematically assigned/aggregated across that mapping structure at corpus level, rather than shown only illustratively.
- Gate 3 — synthesis use: the mapped distributions, concentrations, gaps, patterns, or cross-category relations are interpreted as substantive synthesis results.

**DO NOT CODE WHEN**
- Do not code a taxonomy, table, matrix, or evidence-map display that merely organizes/presents extracted information without a substantive corpus-level mapping synthesis.
- Do not infer from the publication calling itself a survey/mapping paper unless the three mapping-synthesis gates are met.
- If structured organization exists but it is unclear whether the mapping operation itself constitutes synthesis, use ambiguous rather than forcing a positive value.

**Boundary notes**
- All three mapping-synthesis gates are required: structure, corpus-wide application, and interpretive synthesis use.
- In v0.2.3 a code=1 decision is invalid unless structured dms_gate_checks provide evidence for all three gates.
- A produced EvidenceMap artifact and DescriptiveMappingSynthesis are independent decisions; either can occur without the other.

**Positive examples**
- A review assigns all included sources to defined categories, reports category frequencies/distributions, and interprets concentrations/gaps.
- A review maps all guidance documents across process stages/topic areas and interprets which areas are covered or missing.

**Negative examples**
- A taxonomy or table displays extracted categories but no corpus-wide assignment/distribution is synthesized.
- A few publication-year counts are shown without systematic mapping and interpretive use.

### `revmeta:usesSynthesisMethod.ThematicSynthesis` — Thematic synthesis

**Depth:** `CORE_FACET`  
**Definition:** A synthesis method that develops or synthesizes themes across qualitative or textual evidence.

**CODE WHEN**
- The source explicitly uses thematic synthesis/analysis as the synthesis procedure.

**DO NOT CODE WHEN**
- Open/axial/grounded coding is not automatically ThematicSynthesis.
- Do not infer from results being organized under headings/themes without a thematic method.

**Boundary notes**
- Require theme development/synthesis across textual evidence.
- Do not silently normalize generic content analysis or open/axial coding into thematic synthesis.

**Positive examples**
- The methods/results show thematic synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling thematic synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.FrameworkSynthesis` — Framework synthesis

**Depth:** `CORE_FACET`  
**Definition:** A synthesis method that systematically codes, organizes, maps, or interprets evidence across sources through an explicit analytical/a priori framework.

**CODE WHEN**
- The review explicitly uses framework synthesis with substantive cross-source realization; OR evidence across the corpus/subcorpus is systematically coded/organized through a defined analytical framework.

**DO NOT CODE WHEN**
- Do not infer from producing/displaying a framework.
- Do not code a one-off/local comparison of findings to a standard/framework when the main synthesis is another method and the framework is not a systematic synthesis structure.

**Boundary notes**
- A priori framework-based coding across evidence qualifies even when paired with thematic analysis; local framework reference does not.

**Positive examples**
- The methods/results show framework synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling framework synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.MetaAnalysis` — Meta-analysis

**Depth:** `CORE_FACET`  
**Definition:** A quantitative synthesis method that statistically combines effect estimates or comparable quantitative results across studies.

**CODE WHEN**
- The review statistically pools or meta-analyzes effect estimates/results.

**DO NOT CODE WHEN**
- Do not code simple descriptive statistics or counts.

**Boundary notes**
- Statistical combination of comparable quantitative estimates is required; reporting pooled results from another review is insufficient.
- EffectEstimate object type is independently coded when estimates themselves are analytical objects.

**Positive examples**
- The methods/results show meta-analysis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling meta-analysis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.QualitativeMetaSynthesis` — Qualitative meta-synthesis

**Depth:** `CORE_FACET`  
**Definition:** A qualitative synthesis method explicitly described as qualitative meta-synthesis or an equivalent meta-synthetic procedure.

**CODE WHEN**
- The source explicitly identifies and performs qualitative meta-synthesis.

**DO NOT CODE WHEN**
- Do not use as a generic label for any qualitative synthesis.

**Boundary notes**
- Require an explicit qualitative meta-synthesis or methodologically equivalent meta-synthetic procedure; generic qualitative summary is insufficient.

**Positive examples**
- The methods/results show qualitative meta-synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling qualitative meta-synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.MixedMethodsSynthesis` — Mixed-methods synthesis

**Depth:** `CORE_FACET`  
**Definition:** A synthesis method that explicitly integrates quantitative and qualitative evidence or synthesis components within one mixed-methods synthesis.

**CODE WHEN**
- The review explicitly integrates qualitative and quantitative synthesis components.

**DO NOT CODE WHEN**
- Do not code merely because the corpus contains both qualitative and quantitative studies.

**Boundary notes**
- Requires explicit integration of quantitative and qualitative synthesis components.
- Do not infer from an IntegrativeReviewDesign or a mixed corpus alone.

**Positive examples**
- The methods/results show mixed-methods synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling mixed-methods synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.RealistSynthesis` — Realist synthesis

**Depth:** `CORE_FACET`  
**Definition:** A synthesis method that explains how outcomes arise through mechanisms in contexts using realist synthesis logic.

**CODE WHEN**
- The synthesis explicitly uses realist context-mechanism-outcome or equivalent realist explanatory analysis.

**DO NOT CODE WHEN**
- Do not infer from generic discussion of context and mechanisms.

**Boundary notes**
- Requires realist context-mechanism-outcome or equivalent explanatory integration.
- Can coexist with RealistReviewDesign but neither entails the other automatically.

**Positive examples**
- The methods/results show realist synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling realist synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.BibliometricNetworkSynthesis` — Bibliometric/network synthesis

**Depth:** `CORE_FACET`  
**Definition:** A substantive bibliometric/scientometric or network synthesis that integrates publication/citation/co-authorship/co-word or related metadata to characterize corpus-level structure, relationships, or trends; routine publication counts alone are insufficient.

**CODE WHEN**
- The review performs bibliometric/network analysis as a substantive synthesis.

**DO NOT CODE WHEN**
- Publication-year counts alone do not necessarily establish network/bibliometric synthesis unless used as a substantive bibliometric analysis.

**Boundary notes**
- Routine publication-year counts alone are insufficient.
- BibliographicMetadata analytical object may be positive even when the synthesis method is only descriptive mapping rather than bibliometric/network synthesis.

**Positive examples**
- The methods/results show bibliometric/network synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling bibliometric/network synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.MetaNarrativeSynthesis` — Meta-narrative synthesis

**Depth:** `CORE_FACET`  
**Definition:** A synthesis method that compares and integrates the narratives, paradigms, or trajectories of distinct research traditions.

**CODE WHEN**
- The review explicitly performs meta-narrative synthesis across research traditions.

**DO NOT CODE WHEN**
- Do not equate with generic narrative synthesis.

**Boundary notes**
- Requires synthesis across research traditions/narratives.
- Distinguish from MetaNarrativeReviewDesign.

**Positive examples**
- The methods/results show meta-narrative synthesis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling meta-narrative synthesis, but it does not perform substantive cross-source synthesis by that method.

### `revmeta:usesSynthesisMethod.QualitativeContentAnalysis` — Qualitative content analysis

**Depth:** `CORE_FACET`  
**Definition:** A synthesis method using explicit qualitative content-analysis procedures to code and interpret textual material across the evidence corpus.

**CODE WHEN**
- The source explicitly uses content analysis as a synthesis/analysis method.

**DO NOT CODE WHEN**
- Do not silently map content analysis to ThematicSynthesis.

**Boundary notes**
- Require explicit systematic content coding/analysis across sources.
- Do not automatically co-code ThematicSynthesis unless theme-generation criteria are independently met.

**Positive examples**
- The methods/results show qualitative content analysis being used to integrate evidence across multiple included sources.

**Negative examples**
- The paper uses a presentation or analysis element resembling qualitative content analysis, but it does not perform substantive cross-source synthesis by that method.

## revmeta:hasExecutionMode — execution mode

**Tier:** `CORE_FACET`  
**Definition:** Relates the review investigation to an explicit accelerated execution mode intended to shorten the review process through a recognized rapid-review approach.

**Boundary:** Rapid execution can coexist with a separately coded review design.

### `revmeta:hasExecutionMode.RapidExecutionMode` — Rapid execution mode

**Depth:** `CORE_FACET`  
**Definition:** A process modifier indicating that the review deliberately uses an accelerated or rapid review approach.

**CODE WHEN**
- The source explicitly identifies a rapid review/rapid evidence synthesis or deliberate rapid execution strategy.

**DO NOT CODE WHEN**
- Do not infer merely from a short publication timeline.
- If no positive rapid modifier is reported after relevant sections are checked, record no positive assertion rather than treating ordinary review as a separate value.

**Boundary notes**
- Short duration alone is insufficient; rapid/accelerated mode must be intentional and explicit.

**Positive examples**
- The authors explicitly call the study a rapid review and describe accelerated review procedures.

**Negative examples**
- The review was completed quickly, but no rapid-review execution mode is claimed or described.

## revmeta:hasUpdateMode — update mode

**Tier:** `CORE_FACET`  
**Definition:** Relates the review investigation to an explicit living/continuous update mode in which the evidence synthesis is intended to be updated as new evidence becomes available.

**Boundary:** Living update mode is orthogonal to review design and publication function.

### `revmeta:hasUpdateMode.LivingUpdateMode` — Living update mode

**Depth:** `CORE_FACET`  
**Definition:** A process modifier indicating an intentionally ongoing review that is planned to be updated as new evidence becomes available.

**CODE WHEN**
- The source explicitly identifies the review as living or specifies an ongoing update mechanism.

**DO NOT CODE WHEN**
- A one-off update of an earlier review is insufficient.
- A rerunnable repository alone does not imply living mode.

**Boundary notes**
- A one-off updated review is not living; ongoing update commitment is required.

**Positive examples**
- The authors state that the review is living and will be updated as new evidence appears.

**Negative examples**
- The publication is a one-time update of an older review with no ongoing update commitment.

## revmeta:hasRegistrationStatus — registration status

**Tier:** `OPTIONAL_DETAIL`  
**Definition:** Classifies whether the review is explicitly registered in a formal review registry/comparable registration system or explicitly states that it was not registered.

**Boundary:** Registration status is optional detail; timing is a qualifier, not an additional status value.

### `revmeta:hasRegistrationStatus.Registered` — Registered

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** The review investigation is explicitly registered in a review registry or comparable formal registration system.

**CODE WHEN**
- A registry record or registration identifier is reported.

**DO NOT CODE WHEN**
- A published protocol alone is not equivalent to registration.
- Do not infer prospective timing from a registration number alone.

**Boundary notes**
- A protocol publication is not registration.
- Registration timing is a separate qualifier; a registration number alone does not prove prospective timing.

**Positive examples**
- The methods provide a registry name and registration identifier for the review.

**Negative examples**
- A protocol article is cited, but no registry registration is reported.

### `revmeta:hasRegistrationStatus.ExplicitlyNotRegistered` — Explicitly not registered

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** The publication explicitly states that the review was not registered.

**CODE WHEN**
- The source explicitly states no registration/not registered.

**DO NOT CODE WHEN**
- Absence of registration information is not this value; it is a non-positive/NotReported assessment.

**Boundary notes**
- Silence is not explicit non-registration.

**Positive examples**
- The authors explicitly state that the review was not registered.

**Negative examples**
- The paper says nothing about registration.

## revmeta:hasAgentConfiguration — agent configuration

**Tier:** `OPTIONAL_DETAIL`  
**Definition:** Relates specified review workflow stages to the human, automated, or integrated human-machine configuration that performs substantive work at those stages.

**Boundary:** The primary boundary is AutomatedAgent versus HybridHumanMachine, plus coexistence of SingleHumanReviewer and MultipleHumanReviewers within a stage when procedures differ by substage.

### `revmeta:hasAgentConfiguration.SingleHumanReviewer` — Single human reviewer

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A workflow stage is performed by one human reviewer/analyst.

**CODE WHEN**
- The source explicitly states that one person performed the specified workflow stage.

**DO NOT CODE WHEN**
- Do not infer from authorship count.
- Always pair with workflow_stage.

**Boundary notes**
- May coexist with MultipleHumanReviewers at the same broad stage when distinct substages are explicitly reported.
- Always qualify by workflow stage.

**Positive examples**
- The methods explicitly state that a single human reviewer configuration performed a specified workflow stage, and the stage is recorded.

**Negative examples**
- The publication has evidence of single human reviewer only by inference from authorship or generic software use, not an explicit stage-qualified workflow description.

### `revmeta:hasAgentConfiguration.MultipleHumanReviewers` — Multiple human reviewers

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A workflow stage is performed, checked, duplicated, or resolved by multiple human reviewers/analysts.

**CODE WHEN**
- The source explicitly states independent, duplicate, consensus, checked, or collaborative human work at the specified stage.

**DO NOT CODE WHEN**
- Do not infer from multiple authors.
- Always pair with workflow_stage.

**Boundary notes**
- Do not infer from author count.
- Independent duplicate work, consensus, checking, or collaborative execution may support this value depending on the described stage.

**Positive examples**
- The methods explicitly state that a multiple human reviewers configuration performed a specified workflow stage, and the stage is recorded.

**Negative examples**
- The publication has evidence of multiple human reviewers only by inference from authorship or generic software use, not an explicit stage-qualified workflow description.

### `revmeta:hasAgentConfiguration.AutomatedAgent` — Automated agent

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A stage-qualified configuration in which software or an algorithm executes a substantive review task without concurrent substantive human judgment in that execution step, although humans may configure, supervise, or review outputs before/afterward.

**CODE WHEN**
- A substantive review task at a specified workflow stage is executed by software/algorithmic automation without concurrent substantive human judgment in that execution step.

**DO NOT CODE WHEN**
- Do not code passive database/search/reference-management software.
- Do not use when human and machine make integrated substantive decisions within the same task; use HybridHumanMachine.

**Boundary notes**
- Passive software/tool use is insufficient.
- Distinguish from HybridHumanMachine by whether substantive human judgment is concurrent/interdependent within the same task.

**Positive examples**
- The methods explicitly state that a automated agent configuration performed a specified workflow stage, and the stage is recorded.

**Negative examples**
- The publication has evidence of automated agent only by inference from authorship or generic software use, not an explicit stage-qualified workflow description.

### `revmeta:hasAgentConfiguration.HybridHumanMachine` — Hybrid human-machine

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A stage-qualified configuration in which human and automated/AI agents make substantively interdependent contributions within the same review task or stage, rather than merely using software as a passive tool.

**CODE WHEN**
- At a specified workflow stage, human and automated/AI components make substantively interdependent contributions to the same task.

**DO NOT CODE WHEN**
- Do not code passive software assistance.
- Do not collapse clearly separate human-only and automation-only stages into a hybrid assertion.

**Boundary notes**
- Separate human and automated stages should be represented separately rather than forced into hybrid.
- Require substantive interdependence, not software-assisted administration.

**Positive examples**
- The methods explicitly state that a hybrid human-machine configuration performed a specified workflow stage, and the stage is recorded.

**Negative examples**
- The publication has evidence of hybrid human-machine only by inference from authorship or generic software use, not an explicit stage-qualified workflow description.

## revmeta:claimsContributionType — claimed contribution type

**Tier:** `OPTIONAL_DETAIL`  
**Definition:** Relates the review publication to types of scholarly contribution that the authors explicitly present as principal value added by the work and materially realize.

**Boundary:** Claims are about principal value added, not merely what the paper does or contains. Type-fit overrides labels. Publication function and output artifact remain separate.

### `revmeta:claimsContributionType.TaxonomyContribution` — Taxonomy contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that introduces, substantially revises, or consolidates a structured classification scheme whose categories and organizing distinctions classify phenomena in the reviewed domain.

**CODE WHEN**
- Gate 1 — central contribution/value-added evidence explicitly presents a classification/categorization scheme as a principal output, even if authors label it a “classification framework”.
- Gate 2 — the output uses explicit categories, dimensions, distinctions or assignment principles to classify phenomena.
- Gate 3 — the classification is materially developed.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- Type-fit overrides label: a “classification framework” can be TaxonomyContribution when its substantive function is classification.

**Positive examples**
- The abstract or contribution statement explicitly presents a taxonomy contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal taxonomy contribution.

### `revmeta:claimsContributionType.FrameworkContribution` — Framework contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that introduces, substantially revises, or consolidates an organizing structure of concepts, components, relations, stages, or rules intended to guide analysis, design, evaluation, or understanding.

**CODE WHEN**
- Gate 1 — principal claim: central text explicitly presents a framework as a principal contribution/value added by the publication.
- Gate 2 — type fit: the claimed contribution organizes components/concepts/stages/relations/rules for analysis, design, evaluation, or understanding.
- Gate 3 — realization: the claimed contribution is materially developed in the publication rather than merely promised, mentioned, or implied by an artifact.

**DO NOT CODE WHEN**
- Do not code solely because authors call a classification scheme a framework; if it only partitions phenomena into categories/dimensions, assess TaxonomyContribution.
- Do not infer from FrameworkArtifact presence alone.

**Boundary notes**
- FrameworkContribution requires organizing components/relations/stages/rules beyond classification alone; lexical “framework” is insufficient.

**Positive examples**
- The abstract or contribution statement explicitly presents a framework contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal framework contribution.

### `revmeta:claimsContributionType.ConceptualContribution` — Conceptual contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution consisting of conceptual clarification, synthesis, integration, reframing, or a conceptual model where no more specific controlled contribution type adequately captures the claimed value.

**CODE WHEN**
- Gate 1 — principal claim: central text explicitly presents conceptual clarification, integration, reframing, or conceptual model as a principal contribution/value added by the publication.
- Gate 2 — type fit: the claimed contribution changes or consolidates the conceptual understanding of the domain and is not merely the generic broader label for a more specific taxonomy/framework claim.
- Gate 3 — realization: the claimed contribution is materially developed in the publication rather than merely promised, mentioned, or implied by an artifact.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- Use as the broader conceptual category only when a more specific taxonomy/framework contribution does not better capture the principal claim.

**Positive examples**
- The abstract or contribution statement explicitly presents a conceptual contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal conceptual contribution.

### `revmeta:claimsContributionType.MethodologicalContribution` — Methodological contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that introduces, adapts, systematizes, or critically develops a method, procedure, protocol, or methodological approach as scholarly value added by the review.

**CODE WHEN**
- Central contribution/value-added evidence presents a method, procedure, guideline, checklist, protocol or methodological workflow as principal scholarly value.
- The contribution prescribes/systematizes how research/evaluation/review work should be performed, rather than merely using an existing method.
- The method/guideline is materially developed.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- A structured checklist/guideline for conducting future research/evaluation can qualify as methodological contribution even if not labeled “methodology”.

**Positive examples**
- The abstract or contribution statement explicitly presents a methodological contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal methodological contribution.

### `revmeta:claimsContributionType.DesignArtifactContribution` — Design artifact contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that proposes or develops an engineered/design solution—such as an architecture, prototype, reference design, or design specification—as scholarly value added by the review.

**CODE WHEN**
- Gate 1 — principal claim: central text explicitly presents an engineered/design solution as a principal contribution/value added by the publication.
- Gate 2 — type fit: the claimed contribution proposes or develops an architecture, prototype, reference design, design specification, or comparable designed solution.
- Gate 3 — realization: the claimed contribution is materially developed in the publication rather than merely promised, mentioned, or implied by an artifact.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- Distinguish claimed design contribution from a DesignArtifact object/output.

**Positive examples**
- The abstract or contribution statement explicitly presents a design artifact contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal design artifact contribution.

### `revmeta:claimsContributionType.BenchmarkContribution` — Benchmark contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that introduces or substantially develops a benchmark, benchmarking protocol, evaluation suite, or comparable standardized resource for comparative evaluation.

**CODE WHEN**
- Gate 1 — principal claim: central text explicitly presents a benchmark, benchmarking protocol, or evaluation suite as a principal contribution/value added by the publication.
- Gate 2 — type fit: the claimed contribution creates/substantially develops a standardized comparative-evaluation resource or protocol.
- Gate 3 — realization: the claimed contribution is materially developed in the publication rather than merely promised, mentioned, or implied by an artifact.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- Distinguish claimed contribution from BenchmarkArtifact output and Benchmark analytical object.

**Positive examples**
- The abstract or contribution statement explicitly presents a benchmark contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal benchmark contribution.

### `revmeta:claimsContributionType.ResourceContribution` — Resource contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that provides a reusable research asset—such as a curated dataset, repository, codebase, tool, registry, or structured reference collection—beyond ordinary supplementary material.

**CODE WHEN**
- Central text explicitly frames a curated/reusable collection, repository, dataset, codebase, tool, registry or structured reference collection as value added/resource.
- The resource has material identity/content beyond ordinary supplementary material.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- “We compile/categorize the most exhaustive collection” plus an explicit resource/value claim may satisfy this term even when the resource is embedded rather than separately deposited.

**Positive examples**
- The abstract or contribution statement explicitly presents a resource contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal resource contribution.

### `revmeta:claimsContributionType.ArgumentativeContribution` — Argumentative contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that advances a structured thesis, critique, position, or reasoned argument derived from the review synthesis rather than merely reporting evidence.

**CODE WHEN**
- Gate 1 — principal claim: central text explicitly presents a structured thesis, critique, position, or argument as a principal contribution/value added by the publication.
- Gate 2 — type fit: the claimed contribution advances and supports a reasoned position/critique derived from the synthesis rather than merely interpreting results.
- Gate 3 — realization: the claimed contribution is materially developed in the publication rather than merely promised, mentioned, or implied by an artifact.

**DO NOT CODE WHEN**
- Do not infer a contribution claim solely from the existence of a corresponding artifact, method, section, or recommendation.
- Generic usefulness, ordinary synthesis, incidental outputs, and routine implications are insufficient.
- If the authors make no principal contribution claim of this type, code 0 even when related content is present.

**Boundary notes**
- Ordinary interpretation or critique is insufficient unless a structured argument/position is claimed as principal contribution.
- May overlap with PositionFunction but requires an independent contribution claim.

**Positive examples**
- The abstract or contribution statement explicitly presents a argumentative contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal argumentative contribution.

### `revmeta:claimsContributionType.ResearchAgendaContribution` — Research agenda contribution

**Depth:** `OPTIONAL_DETAIL`  
**Definition:** A principal explicitly claimed contribution that formulates and organizes multiple future research problems, questions, directions, or priorities into a coherent agenda.

**CODE WHEN**
- Central contribution/value-added evidence explicitly claims multiple future research directions/problems/opportunities/priorities.
- The paper materially organizes/develops those directions into a coherent agenda/roadmap/challenges-opportunities structure.

**DO NOT CODE WHEN**
- A future-directions section alone is insufficient when future research is not itself claimed as principal value added.
- Generic future work is insufficient.

**Boundary notes**
- A contribution bullet such as “pinpoint several potential directions” can qualify when a structured multi-item agenda is realized; a routine conclusion cannot.

**Positive examples**
- The abstract or contribution statement explicitly presents a research agenda contribution as a principal contribution and the paper materially realizes it.

**Negative examples**
- A related element appears in the paper, but it is not explicitly claimed as a principal research agenda contribution.

## revmeta:producesOutputArtifact — output artifact

**Tier:** `CORE_FACET`  
**Definition:** Relates the review to discrete, identifiable, reusable or independently referable scholarly artifacts generated as outputs of the review synthesis.

**Boundary:** Discreteness is functional, not file-based. Type-fit overrides labels; multi-typing requires independent structural fit for each type.

### `revmeta:producesOutputArtifact.TaxonomyArtifact` — Taxonomy artifact

**Depth:** `CORE_FACET`  
**Definition:** A discrete classification scheme produced by the review that organizes domain entities or concepts into named categories using explicit distinctions, dimensions, or assignment principles.

**CODE WHEN**
- Gate 1 — production: the artifact is generated by the current review rather than merely analyzed from prior literature.
- Gate 2 — discrete identity: the output passes the DISCRETE_ARTIFACT test and can be identified as a bounded scholarly product even if embedded in the article.
- Gate 3 — type fit: The product classifies domain entities/concepts into explicit categories using meaningful distinctions, dimensions, or assignment principles; a mere labeled list/table is insufficient.

**DO NOT CODE WHEN**
- Ordinary result tables, figures, lists, analysis steps, generic recommendations, or supplementary files without independent scholarly-product identity are insufficient.
- Do not infer a claimsContributionType value automatically from artifact presence.
- Do not multi-type the same product unless it independently satisfies every asserted artifact definition.

**Boundary notes**
- Classification-only structures are TaxonomyArtifact even when authors call them frameworks. Multi-type FrameworkArtifact only if additional organizing relations/rules/stages are genuinely present.

**Positive examples**
- The review produces a named or otherwise discrete taxonomy artifact that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a taxonomy artifact but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.FrameworkArtifact` — Framework artifact

**Depth:** `CORE_FACET`  
**Definition:** A discrete, identifiable organizing or analytical framework produced by the review, with defined components/relations/rules that can be independently referred to or reused beyond an ordinary summary table.

**CODE WHEN**
- The current review produces a bounded organizing structure with dimensions/components/stages/relations/rules that can guide analysis, design, evaluation, implementation or understanding.
- A structured checklist/template/recommendation model can qualify if it has explicit organized dimensions/stages and guiding function.

**DO NOT CODE WHEN**
- Do not code a classification-only scheme that lacks framework structure beyond categories; use TaxonomyArtifact.
- Do not code an unstructured recommendation list.

**Boundary notes**
- Checklist/template form does not disqualify a framework; structure and guiding function control the decision.

**Positive examples**
- The review produces a named or otherwise discrete framework artifact that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a framework artifact but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.ConceptualModelArtifact` — Conceptual model artifact

**Depth:** `CORE_FACET`  
**Definition:** A discrete conceptual model produced by the review that represents concepts/entities and meaningful relationships among them; a simple list or category table is insufficient.

**CODE WHEN**
- A review-produced model/process scheme explicitly represents entities/concepts/stages and meaningful relations among them, and the paper treats it as an output/contribution rather than ordinary illustration.

**DO NOT CODE WHEN**
- Ordinary result tables, figures, lists, analysis steps, generic recommendations, or supplementary files without independent scholarly-product identity are insufficient.
- Do not infer a claimsContributionType value automatically from artifact presence.
- Do not multi-type the same product unless it independently satisfies every asserted artifact definition.

**Boundary notes**
- A process diagram may qualify when it is a generalized review-produced model; an ordinary flowchart of the review procedure does not.

**Positive examples**
- The review produces a named or otherwise discrete conceptual model artifact that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a conceptual model artifact but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.DesignArtifact` — Design artifact

**Depth:** `CORE_FACET`  
**Definition:** A discrete engineered or design-oriented output produced by the review, such as an architecture, prototype, reference design, design specification, or comparable solution with identity beyond descriptive analysis.

**CODE WHEN**
- The current review proposes a bounded engineered/design solution such as a method, architecture, reference design or iterative system process with identifiable components/relations.

**DO NOT CODE WHEN**
- Do not code a schematic that merely illustrates prior approaches or generic possibilities without a review-authored proposed design.

**Boundary notes**
- A review-authored “promising method” with specified components and feedback cycle can qualify even if conceptual rather than implemented.

**Positive examples**
- The review produces a named or otherwise discrete design artifact that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a design artifact but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.BenchmarkArtifact` — Benchmark artifact

**Depth:** `CORE_FACET`  
**Definition:** A discrete reusable benchmark, evaluation suite, benchmarking protocol, or reference resource produced by the review to support standardized comparison or evaluation.

**CODE WHEN**
- Gate 1 — production: the artifact is generated by the current review rather than merely analyzed from prior literature.
- Gate 2 — discrete identity: the output passes the DISCRETE_ARTIFACT test and can be identified as a bounded scholarly product even if embedded in the article.
- Gate 3 — type fit: The product is a reusable benchmark, evaluation suite, benchmarking protocol, or reference resource intended to standardize comparative evaluation.

**DO NOT CODE WHEN**
- Ordinary result tables, figures, lists, analysis steps, generic recommendations, or supplementary files without independent scholarly-product identity are insufficient.
- Do not infer a claimsContributionType value automatically from artifact presence.
- Do not multi-type the same product unless it independently satisfies every asserted artifact definition.

**Boundary notes**
- A benchmark discussed or compared is not a produced benchmark artifact.

**Positive examples**
- The review produces a named or otherwise discrete benchmark artifact that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a benchmark artifact but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.ResearchResource` — Research resource

**Depth:** `CORE_FACET`  
**Definition:** A discrete reusable research asset produced or released with the review, such as a curated dataset, codebase, repository, tool, registry, or structured reference collection that has identity beyond ordinary supplementary material.

**CODE WHEN**
- The current review releases or produces a stably identifiable reusable repository, dataset, codebase, tool, registry or structured collection. A named public repository is sufficient evidence of identity when explicitly tied to review artifacts.

**DO NOT CODE WHEN**
- Do not require exhaustive in-paper inventory of every repository file once release and identity are explicit.
- Ordinary supplementary files without reusable research-resource identity remain insufficient.

**Boundary notes**
- Ordinary supplementary files are insufficient unless they constitute a discrete reusable research resource.

**Positive examples**
- The review produces a named or otherwise discrete research resource that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a research resource but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.ResearchAgenda` — Research agenda

**Depth:** `CORE_FACET`  
**Definition:** A discrete structured output that organizes multiple future research questions, problems, directions, or priorities into an identifiable agenda rather than a generic future-work paragraph.

**CODE WHEN**
- The review produces an identifiable organized set of multiple future research questions/problems/challenges/directions/priorities, typically through a dedicated structured section/table/roadmap.

**DO NOT CODE WHEN**
- Generic future-work prose or one/two unstructured suggestions are insufficient.

**Boundary notes**
- A dedicated multi-heading Challenges/Future Directions section can be a ResearchAgenda artifact even without a separate file.

**Positive examples**
- The review produces a named or otherwise discrete research agenda that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles a research agenda but has no discrete artifact identity.

### `revmeta:producesOutputArtifact.EvidenceMap` — Evidence map

**Depth:** `CORE_FACET`  
**Definition:** A discrete structured representation of the distribution of evidence across defined dimensions or questions, intended to show coverage, concentration, and/or gaps; an ordinary results table is insufficient.

**CODE WHEN**
- Gate 1 — production: the artifact is generated by the current review rather than merely analyzed from prior literature.
- Gate 2 — discrete identity: the output passes the DISCRETE_ARTIFACT test and can be identified as a bounded scholarly product even if embedded in the article.
- Gate 3 — type fit: The product is an identifiable structured representation of how evidence is distributed across defined dimensions/questions and is intended to show coverage, concentration, and/or gaps.

**DO NOT CODE WHEN**
- Ordinary result tables, figures, lists, analysis steps, generic recommendations, or supplementary files without independent scholarly-product identity are insufficient.
- Do not infer a claimsContributionType value automatically from artifact presence.
- Do not multi-type the same product unless it independently satisfies every asserted artifact definition.

**Boundary notes**
- An ordinary result matrix/table is insufficient unless it functions as an evidence map showing distribution/coverage/gaps.

**Positive examples**
- The review produces a named or otherwise discrete evidence map that can be independently identified and reused/referred to.

**Negative examples**
- An ordinary table, figure, or discussion passage resembles an evidence map but has no discrete artifact identity.

## revmeta:hasOrganizingLens — organizing lens

**Tier:** `REVIEW`  
**Definition:** Relates the review to an explicit organizing perspective through which relationships among subject-matter levels or layers are synthesized.

**Boundary:** Current singleton vocabulary is domain-sensitive and showed a zero pooled Jaccard in confirmatory evaluation; extension-module treatment is preferable unless revalidated.

### `revmeta:hasOrganizingLens.CrossLayerLens` — Cross-layer lens

**Depth:** `REVIEW`  
**Definition:** An organizing lens in which the review explicitly defines at least two distinct layers/levels of a system or phenomenon and materially synthesizes relationships between them—such as dependencies, interfaces, propagation, feedback, trade-offs, or co-design—rather than merely covering multiple components, axes, or phases.

**CODE WHEN**
- Research-only Gate 1 — the review explicitly defines or operationally distinguishes at least two levels/layers that differ in scope, function, or abstraction and are treated as levels rather than merely categories.
- Research-only Gate 2 — relations between those layers (e.g. dependency, interface, propagation, feedback, trade-off, co-design) are themselves material synthesis targets.
- Both gates must be supported; borderline cases remain ambiguous in FULL_SEMANTIC_AUDIT.

**DO NOT CODE WHEN**
- Do not code mere coverage of multiple axes, components, perspectives, phases, modules, or taxonomy dimensions.
- Do not code when the paper discusses several levels but does not synthesize relationships between them.
- Do not use in CORE_ONLY or CORE_PLUS_OPTIONAL production annotation.

**Boundary notes**
- Require at least two defensibly distinct layers and an explicit relation between them as an object of synthesis.
- Multiple taxonomy axes, train/test phases, components, or perspectives alone are insufficient.
- Because “layer” remains under-specified across domains, retain REVIEW status pending revalidation.

**Positive examples**
- The synthesis explicitly links architecture-level, evaluation-level, and governance-level phenomena and analyzes dependencies/trade-offs among those defined layers.

**Negative examples**
- A taxonomy has two axes or a method has train/test phases, but relationships between distinct layers are not themselves synthesized.
