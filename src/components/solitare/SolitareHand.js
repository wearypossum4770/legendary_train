/** @format */

import cardBack from "../../styles/minified_rear_card_design.svg";
import "../../styles/solitare.css";
export default function SolitareHand() {
  // https://www.valentinog.com/blog/testing-django/
  // https://www.businessinsider.com/resume-template-college-student-get-a-job-at-spotify-2021-4
  // https://www.salesforceben.com/how-to-write-user-stories-for-salesforce/
  // https://cssanimation.rocks/spheres/
  // https://css-tricks.com/webpagetest-api/
  // https://codepen.io/bfa/pen/ggGYeE
  console.log(cardBack);
  return (
    <div className="w3-container">
      <img alt="card deck image - back" className="card-back" src={cardBack} />
    </div>
  );
}
